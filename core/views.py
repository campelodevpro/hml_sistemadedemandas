from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .forms import TaskForm
from .models import Profile, Sector, Task


def profile_for(user):
    return getattr(user, "profile", None)


def accessible_sectors(user):
    profile = profile_for(user)
    if user.is_superuser or (profile and profile.role == Profile.ROLE_ADMIN):
        return Sector.objects.all()
    if not profile:
        return Sector.objects.none()
    return Sector.objects.filter(
        Q(member_profiles=profile) | Q(manager_profiles=profile)
    ).distinct()


def manageable_sectors(user):
    profile = profile_for(user)
    if user.is_superuser or (profile and profile.role == Profile.ROLE_ADMIN):
        return Sector.objects.all()
    if profile and profile.role == Profile.ROLE_MANAGER:
        return profile.managed_sectors.all()
    return Sector.objects.none()


def scoped_tasks(user):
    profile = profile_for(user)
    if user.is_superuser or (profile and profile.role == Profile.ROLE_ADMIN):
        return Task.objects.all()
    return Task.objects.filter(
        Q(sector__in=accessible_sectors(user))
        | Q(status=Task.STATUS_DRAFT, creator=user)
    ).distinct()


def risk_for(task):
    if task.status == Task.STATUS_DONE or not task.due_date:
        return "green"
    today = timezone.localdate()
    if task.due_date < today:
        return "red"
    if (
        task.status == Task.STATUS_IN_PROGRESS
        and task.last_activity_at < timezone.now() - timedelta(days=3)
    ):
        return "yellow"
    total_days = max((task.due_date - task.created_at.date()).days, 1)
    remaining_days = (task.due_date - today).days
    if remaining_days <= total_days * 0.2 and task.status in {
        Task.STATUS_BACKLOG,
        Task.STATUS_TODO,
    }:
        return "yellow"
    return "green"


def task_columns(tasks):
    labels = [
        (Task.STATUS_BACKLOG, "Backlog"),
        (Task.STATUS_TODO, "A Fazer"),
        (Task.STATUS_IN_PROGRESS, "Em Andamento"),
        (Task.STATUS_DONE, "Concluido"),
    ]
    columns = []
    for status, label in labels:
        items = [task for task in tasks if task.status == status]
        for task in items:
            task.risk = risk_for(task)
        columns.append({"status": status, "label": label, "tasks": items})
    return columns


@login_required
def board(request):
    tasks = list(
        scoped_tasks(request.user)
        .select_related("assignee", "project", "sector")
        .exclude(status=Task.STATUS_DRAFT)
    )
    context = {
        "columns": task_columns(tasks),
        "total_tasks": len(tasks),
        "in_progress": sum(task.status == Task.STATUS_IN_PROGRESS for task in tasks),
        "overdue": sum(risk_for(task) == "red" for task in tasks),
        "profile": profile_for(request.user),
        "manageable_sectors": manageable_sectors(request.user),
    }
    return render(request, "core/board.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def task_create(request):
    form = TaskForm(
        request.POST or None, allowed_sectors=accessible_sectors(request.user)
    )
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.creator = request.user
        task.unit = task.sector.unit if task.sector_id else None
        task.save()
        messages.success(request, "Demanda salva com sucesso.")
        return redirect("board")
    return render(request, "core/task_form.html", {"form": form})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(scoped_tasks(request.user), pk=pk)
    if (
        task.is_private_draft
        and task.creator_id != request.user.id
        and not request.user.is_staff
    ):
        return redirect("board")
    return render(request, "core/task_detail.html", {"task": task})


@login_required
@require_http_methods(["GET", "POST"])
def team_manage(request, pk):
    sector = get_object_or_404(Sector.objects.select_related("unit"), pk=pk)
    if not manageable_sectors(request.user).filter(pk=sector.pk).exists():
        raise PermissionDenied
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        action = request.POST.get("action")
        user = get_object_or_404(get_user_model(), pk=member_id)
        if action == "add":
            profile, _ = Profile.objects.get_or_create(user=user)
            sector.member_profiles.add(profile)
            messages.success(request, "Colaborador adicionado a equipe.")
        elif action == "remove":
            sector.member_profiles.filter(user=user).delete()
            messages.success(request, "Colaborador removido da equipe.")
        return redirect("team_manage", pk=sector.pk)
    members = sector.member_profiles.select_related("user").order_by("user__email")
    available_users = (
        get_user_model()
        .objects.exclude(profile__in=sector.member_profiles.all())
        .order_by("email")
    )
    return render(
        request,
        "core/team_manage.html",
        {"sector": sector, "members": members, "available_users": available_users},
    )

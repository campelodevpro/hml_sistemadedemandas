from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .forms import TaskForm
from .models import Profile, Task


def profile_for(user):
    return getattr(user, "profile", None)


def scoped_tasks(user):
    profile = profile_for(user)
    if user.is_superuser or (profile and profile.role == Profile.ROLE_ADMIN):
        return Task.objects.all()
    if not profile or not profile.unit_id:
        return Task.objects.filter(Q(creator=user) | Q(assignee=user))
    scope = Q(unit_id=profile.unit_id)
    if profile.sector_id:
        scope &= Q(sector_id=profile.sector_id)
    return Task.objects.filter(scope)


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
    }
    return render(request, "core/board.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        profile = profile_for(request.user)
        if not profile or not profile.unit_id:
            messages.error(
                request, "Seu usuario ainda nao esta vinculado a uma unidade."
            )
            return render(request, "core/task_form.html", {"form": form})
        task = form.save(commit=False)
        task.creator = request.user
        task.unit_id = profile.unit_id
        if not task.sector_id:
            task.sector_id = profile.sector_id
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

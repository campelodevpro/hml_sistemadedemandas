import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.models import Profile, Sector, Task, Unit

User = get_user_model()


@pytest.fixture
def user_with_scope(db):
    user = User.objects.create_user(
        email="leonardo@example.test", password="senha-segura-123"
    )
    unit = Unit.objects.create(name="UTIC")
    sector = Sector.objects.create(unit=unit, name="Sistemas")
    profile = Profile.objects.create(user=user, role=Profile.ROLE_MANAGER)
    profile.member_sectors.add(sector)
    profile.managed_sectors.add(sector)
    return user, unit, sector


@pytest.mark.django_db
def test_board_shows_only_tasks_from_users_sector(client, user_with_scope):
    user, unit, sector = user_with_scope
    other_unit = Unit.objects.create(name="Outra unidade")
    own = Task.objects.create(
        title="Demanda visivel", creator=user, unit=unit, sector=sector
    )
    Task.objects.create(title="Demanda fora do escopo", creator=user, unit=other_unit)
    client.force_login(user)
    response = client.get(reverse("board"))
    assert response.status_code == 200
    body = response.content.decode()
    assert own.title in body
    assert "Demanda fora do escopo" not in body


@pytest.mark.django_db
def test_incomplete_task_can_be_saved_as_private_draft(client, user_with_scope):
    user, _, _ = user_with_scope
    client.force_login(user)
    response = client.post(
        reverse("task_create"),
        {"title": "Melhorar Avisos", "status": Task.STATUS_DRAFT, "priority": "MEDIUM"},
    )
    assert response.status_code == 302
    draft = Task.objects.get(title="Melhorar Avisos")
    assert draft.status == Task.STATUS_DRAFT
    assert draft.creator_id == user.id
    assert (
        not Task.objects.exclude(status=Task.STATUS_DRAFT).filter(pk=draft.pk).exists()
    )


@pytest.mark.django_db
def test_complete_task_can_start_directly_in_progress(client, user_with_scope):
    user, _, sector = user_with_scope
    assignee = User.objects.create_user(
        email="carlos@example.test", password="senha-segura-123"
    )
    client.force_login(user)
    response = client.post(
        reverse("task_create"),
        {
            "title": "Criacao dos scripts de migracao em Python",
            "assignee": assignee.id,
            "sector": sector.id,
            "status": Task.STATUS_IN_PROGRESS,
            "priority": "HIGH",
            "due_date": "2030-01-03",
        },
    )
    assert response.status_code == 302
    assert (
        Task.objects.get(title__startswith="Criacao dos scripts").status
        == Task.STATUS_IN_PROGRESS
    )


@pytest.mark.django_db
def test_login_accepts_email(client, user_with_scope):
    user, _, _ = user_with_scope

    response = client.post(
        reverse("login"),
        {"username": user.email, "password": "senha-segura-123"},
    )

    assert response.status_code == 302
    assert client.session.get("_auth_user_id") == str(user.id)


def test_user_uses_unique_email_as_login_identifier():
    assert User.USERNAME_FIELD == "email"
    assert User._meta.get_field("email").unique is True


@pytest.mark.django_db
def test_user_with_multiple_sectors_sees_combined_tasks(client, user_with_scope):
    user, unit, first_sector = user_with_scope
    second_sector = Sector.objects.create(unit=unit, name="Infraestrutura")
    other_sector = Sector.objects.create(unit=unit, name="Financeiro")
    user.profile.member_sectors.add(second_sector)
    first = Task.objects.create(
        title="Tarefa de sistemas", creator=user, unit=unit, sector=first_sector
    )
    second = Task.objects.create(
        title="Tarefa de infraestrutura", creator=user, unit=unit, sector=second_sector
    )
    Task.objects.create(
        title="Tarefa financeira", creator=user, unit=unit, sector=other_sector
    )

    client.force_login(user)
    response = client.get(reverse("board"))

    body = response.content.decode()
    assert first.title in body
    assert second.title in body
    assert "Tarefa financeira" not in body


@pytest.mark.django_db
def test_manager_can_manage_only_sectors_assigned_to_management(
    client, user_with_scope
):
    manager, unit, managed_sector = user_with_scope
    other_sector = Sector.objects.create(unit=unit, name="Comercial")
    colleague = User.objects.create_user(
        email="ana@example.test", password="senha-segura-123"
    )
    Profile.objects.create(user=colleague, role=Profile.ROLE_RESPONSIBLE)

    client.force_login(manager)
    response = client.post(
        reverse("team_manage", args=[managed_sector.pk]),
        {"action": "add", "member_id": colleague.pk},
    )

    assert response.status_code == 302
    assert managed_sector.member_profiles.filter(user=colleague).exists()
    forbidden = client.get(reverse("team_manage", args=[other_sector.pk]))
    assert forbidden.status_code == 403


@pytest.mark.django_db
def test_superuser_can_manage_any_team(client, user_with_scope):
    _, _, sector = user_with_scope
    superuser = User.objects.create_superuser(
        email="admin@example.test", password="senha-segura-123"
    )

    client.force_login(superuser)
    response = client.get(reverse("team_manage", args=[sector.pk]))

    assert response.status_code == 200
    assert "Equipe: Sistemas" in response.content.decode()


@pytest.mark.django_db
def test_administrator_profile_can_manage_any_team(client, user_with_scope):
    _, _, sector = user_with_scope
    administrator = User.objects.create_user(
        email="gestora@example.test", password="senha-segura-123"
    )
    Profile.objects.create(user=administrator, role=Profile.ROLE_ADMIN)
    administrator.refresh_from_db()

    client.force_login(administrator)
    response = client.get(reverse("team_manage", args=[sector.pk]))

    assert administrator.is_staff is True
    assert response.status_code == 200

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
    Profile.objects.create(
        user=user, role=Profile.ROLE_MANAGER, unit=unit, sector=sector
    )
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
    user, _, _ = user_with_scope
    assignee = User.objects.create_user(
        email="carlos@example.test", password="senha-segura-123"
    )
    client.force_login(user)
    response = client.post(
        reverse("task_create"),
        {
            "title": "Criacao dos scripts de migracao em Python",
            "assignee": assignee.id,
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

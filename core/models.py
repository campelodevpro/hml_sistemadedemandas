from django.conf import settings
from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Sector(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name="sectors")
    name = models.CharField(max_length=120)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["unit", "name"], name="unique_sector_per_unit"
            )
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.unit} / {self.name}"


class Profile(models.Model):
    ROLE_ADMIN = "ADMIN"
    ROLE_MANAGER = "MANAGER"
    ROLE_RESPONSIBLE = "RESPONSIBLE"
    ROLE_CHOICES = [
        (ROLE_ADMIN, "Administrador"),
        (ROLE_MANAGER, "Gerente"),
        (ROLE_RESPONSIBLE, "Responsavel"),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default=ROLE_RESPONSIBLE
    )
    member_sectors = models.ManyToManyField(
        Sector,
        blank=True,
        related_name="member_profiles",
        verbose_name="setores membro",
    )
    managed_sectors = models.ManyToManyField(
        Sector,
        blank=True,
        related_name="manager_profiles",
        verbose_name="setores gerenciados",
    )
    technical_level = models.CharField(max_length=40, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.ROLE_ADMIN and not self.user.is_staff:
            self.user.is_staff = True
            self.user.save(update_fields=["is_staff"])

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.email} ({self.get_role_display()})"


class Project(models.Model):
    PRIORITY_CHOICES = [
        ("LOW", "Baixa"),
        ("MEDIUM", "Media"),
        ("HIGH", "Alta"),
        ("MAX", "Maxima"),
    ]
    name = models.CharField(max_length=180)
    context = models.TextField(blank=True)
    impact = models.CharField(max_length=180, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="MEDIUM"
    )
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name="projects")
    sector = models.ForeignKey(
        Sector, on_delete=models.PROTECT, null=True, blank=True, related_name="projects"
    )
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_DRAFT = "DRAFT"
    STATUS_BACKLOG = "BACKLOG"
    STATUS_TODO = "TODO"
    STATUS_IN_PROGRESS = "IN_PROGRESS"
    STATUS_DONE = "DONE"
    STATUS_CHOICES = [
        (STATUS_DRAFT, "Rascunho"),
        (STATUS_BACKLOG, "Backlog"),
        (STATUS_TODO, "A Fazer"),
        (STATUS_IN_PROGRESS, "Em Andamento"),
        (STATUS_DONE, "Concluido"),
    ]
    PRIORITY_CHOICES = [
        ("LOW", "Baixa"),
        ("MEDIUM", "Media"),
        ("HIGH", "Alta"),
        ("MAX", "Maxima"),
    ]
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks"
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_tasks"
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )
    unit = models.ForeignKey(
        Unit, on_delete=models.PROTECT, null=True, blank=True, related_name="tasks"
    )
    sector = models.ForeignKey(
        Sector, on_delete=models.PROTECT, null=True, blank=True, related_name="tasks"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_BACKLOG
    )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="MEDIUM"
    )
    due_date = models.DateField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_activity_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["due_date", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def is_private_draft(self):
        return self.status == self.STATUS_DRAFT

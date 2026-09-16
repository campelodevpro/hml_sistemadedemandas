from django.urls import path

from . import views

urlpatterns = [
    path("", views.board, name="board"),
    path("tarefas/nova/", views.task_create, name="task_create"),
    path("tarefas/<int:pk>/", views.task_detail, name="task_detail"),
]

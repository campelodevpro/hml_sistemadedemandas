from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "project",
            "assignee",
            "status",
            "priority",
            "due_date",
        ]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("status") != Task.STATUS_DRAFT:
            if not cleaned.get("assignee"):
                self.add_error(
                    "assignee", "Escolha um responsavel ou salve como rascunho."
                )
            if not cleaned.get("due_date"):
                self.add_error("due_date", "Informe um prazo ou salve como rascunho.")
        return cleaned

from django import forms

from .models import Sector, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "project",
            "sector",
            "assignee",
            "status",
            "priority",
            "due_date",
        ]

    def __init__(self, *args, allowed_sectors=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sector"].queryset = allowed_sectors or Sector.objects.none()

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("status") != Task.STATUS_DRAFT:
            if not cleaned.get("sector"):
                self.add_error("sector", "Escolha o setor da demanda.")
            if not cleaned.get("assignee"):
                self.add_error(
                    "assignee", "Escolha um responsavel ou salve como rascunho."
                )
            if not cleaned.get("due_date"):
                self.add_error("due_date", "Informe um prazo ou salve como rascunho.")
        return cleaned

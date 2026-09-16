from django.contrib import admin

from .models import Profile, Project, Sector, Task, Unit

admin.site.register(Unit)
admin.site.register(Sector)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)

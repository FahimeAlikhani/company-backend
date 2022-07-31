from django.contrib import admin

from .models import ProjectRequest , NewsLetterForm

@admin.register(ProjectRequest,NewsLetterForm)

class ProjectRequest(admin.ModelAdmin):
    pass

class NewLetterForm(admin.ModelAdmin):
    pass


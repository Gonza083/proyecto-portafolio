from django.contrib import admin

from.models import Project   

class ProjectAdmin(admin.ModelAdmin):
    readony_fields = ('created', 'updated')

admin.site.register(Project,ProjectAdmin )

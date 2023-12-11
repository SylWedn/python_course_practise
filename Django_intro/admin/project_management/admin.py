from django.contrib import admin
from .models import Project, Label


class AdminProject(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'get_owner_username')
    search_fields = ('code', 'name', 'description', 'owner__username', 'label__name')
    list_editable = ('description', 'name')

    @admin.display(ordering='owner__username', description='Username')
    def get_owner_username(self, obj):
        return obj.owner.username


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, AdminProject)
admin.site.register(Label, LabelAdmin)



from django.contrib import admin
from .models import User
from project_management.models import Project


class ProjectInLine(admin.TabularInline):
    model = Project
    extra = 0
    can_delete = False
    readonly_fields = ('code', )


class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'last_login')
    list_filter = ('is_superuser', 'is_active')

    fieldsets = (
        ('General', {'fields': ('password', 'username')}),
        ('Superuser', {'fields': ('is_superuser', 'is_staff')}),
    )
    inlines = [ProjectInLine]


admin.site.register(User, AdminUser)

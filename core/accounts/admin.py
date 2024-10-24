from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    """ custom admin panel for user management with add and change forms plus password """
    model = User
    list_display = ('email', 'is_superuser', 'is_active', 'is_verified')
    list_filter = ('email', 'is_superuser', 'is_active', 'is_verified')
    search_fields = ('email',)
    ordering = ('email',)
    # fieldsets are for current users lists
    fieldsets = (
        (
            'Authentication',
            {
                'fields': ('email', 'password'),
            },
        ),
        (
            'permissions',
            {
                'fields': ('is_staff', 'is_active', 'is_superuser', 'is_verified'),
            },
        ),
    )

    # group permissions
    (
        'group permissions',
        {'fields': ('group', 'user_permissions')},
    )

    (
        'important date',
        {'fields': ('last_login',)},
    )

    # add_fieldsets are for making new users
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                    'is_verified',
                ),
            },
        ),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)
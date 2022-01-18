from django.contrib import admin
from authapp.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email',)
    ordering = ('email',)
    list_filter = ('email', 'is_staff')
    list_display = ('email', 'is_active', 'is_staff', 'opt_in')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'opt_in')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'opt_in')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)

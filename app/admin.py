from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','phone','frist_name','last_name','gender','age', 'is_staff', 'is_active',)
    list_filter = ('email','phone','frist_name','last_name','gender','age', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','phone','frist_name','last_name','gender','age',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
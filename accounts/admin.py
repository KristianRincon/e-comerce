from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'address', 'is_staff', 'is_active']
    
    # Convertir a listas antes de añadir campos personalizados
    fieldsets = list(UserAdmin.fieldsets) + [
        (None, {'fields': ('phone_number', 'address')}),
    ]
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (None, {'fields': ('phone_number', 'address')}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)
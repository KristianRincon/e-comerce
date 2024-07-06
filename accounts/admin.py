from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm #Formulario para agregar nuevos usuarios
    form = CustomUserChangeForm # Formulario para cambiar detalles de usuarios existentes
    model = CustomUser # Modelo de usuario que se esta administrando
    list_display = ['username', 'email', 'phone_number', 'address', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address')})
    )

admin.site.register(CustomUser, CustomUserAdmin)
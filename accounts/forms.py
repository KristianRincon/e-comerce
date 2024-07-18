from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'w-full p-2 border border-gray-300 rounded mt-1'}

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'w-full p-2 border border-gray-300 rounded mt-1'}


class CustomAuthenticationForm(AuthenticationForm):
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1', 'placeholder': 'Nombre de usuario'})
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1', 'placeholder': 'Contraseña'})
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded mt-1',
                'placeholder': field.label
            })
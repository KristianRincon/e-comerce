from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CustomAuthenticationForm, CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Te has registrado con exito')
            return redirect('home')
        else:
            messages.error(request, 'Error al registrar tu usuario')
        return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    tempalte_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'inicio de sesión exitoso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Error al iniciar sesión, Verifica tus credenciales!')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Has cerrado sesión correctamente.')
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):  # self-> instancia actual de la clase ProfileView self permite acceder a los atributos y metodos de la instancia
        user = request.user  # obtiene el usuario actualmente autenticado
        print(user)
        form = CustomUserChangeForm(instance=user)
        return render(request, 'profile.html', {'form': form})

    # request ->  Es un objeto de solicitud HTTP que Django pasa automáticamente a cada vista.
    def post(self, request):
        user = request.user
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Tu perfil ha sido actualizado con exito')
            return redirect('home')
        else:
            messages.error(request, 'Error al actualizar tu perfil')
        return render(request, 'profile.html', {'form': form})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_changed')

    def form_valid(self, form):
        messages.success(self.request, '¡Has cambiado tu contraseña!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al cambiar tu contraseña')
        return super().form_invalid(form)


from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = 'password_reset.html'



# from django.contrib.auth.views import PasswordChangeView
# from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin

# class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'registration/password_change_form.html'
#     success_url = reverse_lazy('password_changed')
#     success_message = "Tu contraseña ha sido cambiada exitosamente."

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Cambiar contraseña'
#         return context
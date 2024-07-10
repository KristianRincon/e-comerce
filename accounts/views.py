from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CustomAuthenticationForm, CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'form':form})
    
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    tempalte_name = 'registration/login.html'

class ProfileView(LoginRequiredMixin, View): 
    def get(self, request): # self-> instancia actual de la clase ProfileView self permite acceder a los atributos y metodos de la instancia
        user = request.user #obtiene el usuario actualmente autenticado
        print(user)
        form = CustomUserChangeForm(instance=user)
        return render(request, 'profile.html', {'form':form})
    
    def post(self, request): # request ->  Es un objeto de solicitud HTTP que Django pasa automáticamente a cada vista.
        user = request.user
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'profile.html', {'form':form})
        

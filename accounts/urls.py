from django.urls import path
from .views import CustomLoginView, RegisterView, ProfileView, CustomLogoutView, CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_changed/', PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'), name='password_changed'),
]
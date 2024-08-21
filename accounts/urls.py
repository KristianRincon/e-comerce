from django.urls import path
from .views import CustomLoginView, RegisterView, ProfileView, CustomLogoutView, CustomPasswordChangeView, TestView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_changed/', PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'), name='password_changed'),

    # Recuperar la contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('test/', TestView.as_view(), name='test'),
]
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('register/', views.register_view, name='auth-register'),
    path('login/', views.login_view, name='auth-login'),
    path('logout/', views.logout_view, name='auth-logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html', email_template_name='authentication/password_reset_email.html', subject_template_name='authentication/password_reset_subject.txt'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='authentication/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('verify_email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
    path('deactivate/', views.deactivate_account_view, name='deactivate-account'),
    path('cancel-deletion/<uidb64>/<token>/', views.cancel_deletion_view, name='cancel-deletion'),
]
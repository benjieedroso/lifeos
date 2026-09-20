from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('settings/', TemplateView.as_view(template_name='dashboard/settings.html'), name='settings'),
]

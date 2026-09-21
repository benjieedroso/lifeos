from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

def create_profile_for_new_users(sender, instance, created, **kwargs):
	if created:
		Profile.objects.created(user=instance)
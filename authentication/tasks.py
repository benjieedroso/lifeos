from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone

@shared_task
def delete_account(user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return 'already gone'
    if user.profile.scheduled_deletion_at is None:
        return 'cancelled in time - nothind to do'
    if user.profile.scheduled_deletion_at > timezone.now():
        return 'not due yet - leaving alone'
    email = user.email
    username = user.username
    user.delete()
    send_mail(
        'Your LifeOS account has been deleted',
        f'Hi {username},\n\nYour LifeOS account and all its data were permanently deleted as scheduled.\n\n— The LifeOS Team',
        None,
        [email],
    )

    return f'deleted {username}'
from celery.result import AsyncResult
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse

from authentication.forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User 
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .tasks import delete_account

from lifeos import settings

from .models import Profile


# Create your views here.
def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False  # Deactivate account until it is confirmed
			user.save()
			send_verification_email(user, request)
			return redirect('auth-login')
	else:
		form = RegistrationForm()

	return render(request, 'authentication/register.html', {'page_title': 'Register', 'form': form})


def send_verification_email(user, request):
	uid = urlsafe_base64_encode(force_bytes(user.pk))
	token = default_token_generator.make_token(user)
	verification_link = request.build_absolute_uri(
		reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
	)

	send_mail(
		'Verify your LifeOS account',
		render_to_string('authentication/verify_email_body.txt', {'user': user, 'link': verification_link}),
		settings.DEFAULT_FROM_EMAIL,
		[user.email],
	)



def verify_email(request, uidb64,token):
	try:
		user = User.objects.get(pk=force_str(urlsafe_base64_decode(uidb64)))
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and default_token_generator.check_token(user, token):
		user.is_active = True
		user.save()
		return redirect('auth-login')
	return render(request, 'authentication/verify_failed.html', {'page_title': 'Verification Failed'})


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				request,
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password'],
			)
			if user is not None:
				login(request, user)
				return redirect('dashboard')
			try:
				maybe_user = User.objects.get(username=form.cleaned_data['username'])
				if maybe_user.check_password(form.cleaned_data['password']) and not maybe_user.is_active:
					form.add_error(None, "Your account is inactive. Please verify your email.")
				else:
					form.add_error(None, "Invalid username or password.")
			except User.DoesNotExist:
				form.add_error(None, "Invalid username or password.")
	else:
		form = LoginForm()

	return render(request, 'authentication/login.html', {'page_title': 'Login', 'form': form})


def logout_view(request):
	logout(request)
	return redirect('auth-login')

@login_required
def deactivate_account_view(request):
	if request.method == 'POST':
		user = request.user
		deadline = timezone.now() + timedelta(days=7)

		user.is_active = False
		user.save()

		profile, _ = Profile.objects.get_or_create(user=user)
		profile.scheduled_deletion_at = deadline
		profile.save(update_fields=['scheduled_deletion_at'])

		result = delete_account.apply_async(args=[user.pk], eta=deadline)
		profile.deletion_task_id = result.id
		profile.save(update_fields=['deletion_task_id'])

		send_deactivation_email(request, user, deadline)
		logout(request)
		return redirect('auth-login')

	return render(request, 'dashboard/deactivate_confirm.html')

def send_deactivation_email(request, user, deadline):
	uid = urlsafe_base64_encode(force_bytes(user.pk))
	token = default_token_generator.make_token(user)
	cancel_link = request.build_absolute_uri(
		reverse('cancel-deletion', kwargs={'uidb64': uid, 'token': token})
	)

	send_mail(
        'Your LifeOS account is deactivated',
        render_to_string('authentication/deactivation_email.txt', {
            'user': user,
            'deadline': deadline,
            'cancel_link': cancel_link,
        }),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )



def cancel_deletion_view(request, uidb64, token):
	try:
		user = User.objects.get(pk=force_str(urlsafe_base64_decode(uidb64)))
	except (User.DoesNotExist, ValueError, TypeError, OverflowError):
		user = None
	if user is None or not default_token_generator.check_token(user, token):
		return render(request, 'authentication/verify_failed.html')
	profile, _ = Profile.objects.get_or_create(user=user)
	if profile.scheduled_deletion_at is None:
		return redirect('auth-login')
	if profile.deletion_task_id:
		AsyncResult(profile.deletion_task_id).revoke()
	user.is_active = True
	user.save(update_fields=['is_active'])
	profile.scheduled_deletion_at = None 
	profile.deletion_task_id = None
	profile.save(update_fields=['scheduled_deletion_at', 'deletion_task_id'])
	return redirect('auth-login')
	





# def password_reset_view(request):
# 	if request.method == 'POST':
# 		form = PasswordResetForm(request.POST)
# 		if form.is_valid():
# 			form.save(request=request)
# 			return redirect('password_reset_done')
# 	else:
# 		form = PasswordResetForm()
# 	return render(request, 'authentication/password_reset.html', {'page_title': 'Password Reset', 'form': form})


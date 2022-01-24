from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
	send_mail('Hello There',
		'Hello There this is the message',
		'mjwalls.dev@gmail.com',
		['kexav66840@finxmail.com'],
		fail_silently=False)
	return render(request, 'emails/index.html')
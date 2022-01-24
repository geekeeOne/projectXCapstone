
from django.urls import path
from emailFrog import views


urlpatterns = [
	path('emails/', views.index)
]


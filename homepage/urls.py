from django.urls import path
from . import views 

urlpatterns = [
	path('homepage/', views.members, name='members'),
]



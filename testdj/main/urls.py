
from venv import create
from django.urls import path
from . import views
from users import views as user_views


urlpatterns =  [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('authorization', views.authorization, name='authorization'),

	path('register', user_views.register, name='register'),
]

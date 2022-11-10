
from venv import create
from django.urls import path
from . import views
from . import views as user_views

urlpatterns =  [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
	path('register', user_views.register, name='register'),
    path('logout/',views.logout_user, name='logout'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
]

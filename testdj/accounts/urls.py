from django.contrib.auth import views
from django.urls import path
from . import views

from accounts import views as logout_user
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',logout_user, name='logout')
 ]
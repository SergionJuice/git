from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect ('login')
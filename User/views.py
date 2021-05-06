from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import AuthUserForm, RegisterUserForm


def index(request):
    return render(request, 'User/index.html')


def register(request):
    return render(request, 'User/register.html')


class Login(LoginView):
    fields = ['username', 'password']
    template_name = 'User/login.html'
    form_class = AuthUserForm


class Logout(LogoutView):
    template_name = 'User/logout.html'


class Register(CreateView):
    model = User
    template_name = 'User/register.html'
    form_class = RegisterUserForm
    success_url = '/success_saved'


def success_saved(request):
    return render(request, 'User/success_saved.html')

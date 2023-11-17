from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}! you are able to log in now.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect('home')
            else:
                message = 'Login failed!'
    return render(
        request, 'user/login.html', context={'form': form, 'message': message})
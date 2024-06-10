from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignInForm, RegisterForm
from django.urls import reverse

def sign_in_view(request):
    signin_form = SignInForm()
    if request.method == 'POST' and 'signin' in request.POST:
        signin_form = SignInForm(request, data=request.POST)
        if signin_form.is_valid():
            username = signin_form.cleaned_data.get('username')
            password = signin_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
    return render(request, 'registration/login.html', {'signin_form': signin_form})

def register_view(request):
    register_form = RegisterForm()
    if request.method == 'POST' and 'register' in request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
    return render(request, 'registration/login.html', {'register_form': register_form})

def auth_view(request):
    signin_form = SignInForm()
    register_form = RegisterForm()
    context = {
        'signin_form': signin_form,
        'register_form': register_form,
    }
    return render(request, 'registration/login.html', context)

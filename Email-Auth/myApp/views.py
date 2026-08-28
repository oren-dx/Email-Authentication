from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from myApp.forms import *
from myApp.models import *


def register_view(request):

    form_data = registerForm()

    if request.method == 'POST':
        form_data = registerForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context = {
        'form_data' : form_data
    }

    return render(request, 'register.html', context)


def login_view(request):

    if request.method == 'POST':

        text = request.POST.get('text')
        password = request.POST.get('password')

        try:
            user_data = customAuth.objects.get(username = text)
        except customAuth.DoesNotExist:
            user_data = customAuth.objects.get(email = text)

        print(user_data)

        if user_data:
            user = authenticate(request, username = user_data.username, password = password)

            if user:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'login.html')


def logout_view(reqeust):
    logout(reqeust)
    return redirect('login_view')


def dashboard(request):


    return render(request, 'dashboard.html')
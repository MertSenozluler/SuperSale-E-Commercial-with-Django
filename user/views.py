from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from products.models import *
from django.contrib.auth.models import User
# Create your views here.
def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created')
            return redirect('login')
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request,'Signed in')
            return redirect('index')
        else:
            messages.error(request,'Username or password is wrong')
            return redirect('login')
    return render(request,'login.html')

def userLogout(request):
    logout(request)
    messages.success(request,'Signed out')
    return redirect('index')

def user(request):
    user = request.user
    context = {
        "user":user
    }
    return render(request,'user.html',context)

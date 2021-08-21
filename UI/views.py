from django.shortcuts import render, redirect


def home(request):
    return render (request, 'home.html')


def redirect_home(request):
    return redirect ('/home')

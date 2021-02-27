from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def search(request):
    return render(request, 'search.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
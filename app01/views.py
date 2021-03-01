from django.shortcuts import render


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def search(request):
    return render(request, 'search.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def selfcenter(request):
    return render(request, 'selfcenter.html')


def message_list(request):
    return render(request, 'message_list.html')


def self_profile(request):
    return render(request, 'self_profile.html')

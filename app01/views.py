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


def self_center(request):
    return render(request, 'self_center.html')


def message_list(request):
    return render(request, 'message_list.html')


def profile(request):
    return render(request, 'profile.html')


def favorites(request):
    return render(request, 'favorites.html')

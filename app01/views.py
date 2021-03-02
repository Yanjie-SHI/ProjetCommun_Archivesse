from django.shortcuts import render

from app01.models import Utilisateur


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def search(request):
    if request.method == "GET":
        options = {}
        return render(request, 'search.html', options)
    elif request.method == "POST":
        pass


def search_result(request):
    return render(request, 'search_result.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        options = {}
        user = Utilisateur.objects.get(u_mail=request.POST.get('email'), u_mdp=request.POST.get('password'))
        if user:
            request.session['login_user_name'] = user.u_pseudo
            return render(request, 'search.html')
            # return render(request, 'search.html')
        else:
            return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def self_center(request):
    if request.method == "GET":
        user = request.GET.get("login_user_name")
        if user:
            return render(request, 'self_center.html')
    elif request.method == "POST":
        return render(request, 'self_center.html')


def message_list(request):
    return render(request, 'message_list.html')


def profile(request):
    return render(request, 'profile.html')


def favorites(request):
    return render(request, 'favorites.html')


def reservation(request):
    return render(request, 'reservation.html')


def logout(request):
    request.session.clear()
    return render(request, 'search.html')

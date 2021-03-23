import datetime

from django.shortcuts import render

from app01.utils import *


# Create your views here.


def to_create_demand(request):
    options = verify_login(request)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options.update({"create_date": datetime.datetime.today()})
    return render(request, "demand_create.html", options)


def to_my_demand(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")

    options = verify_login(request)
    # get all my created demand
    demand_list = Demand.objects.filter(demander=options.get("user"))
    if len(demand_list) > 0:
        options.update({"demand_list": demand_list})

    return render(request, 'my_demand.html', options)


def create_demand(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    if request.method == "POST":
        demander = options.get("user")

        # save data in Demand
        demand = Demand()
        demand.create_date = datetime.datetime.now()
        demand.status = 0
        demand.archive_id = request.POST.get("archive_id")
        demand.folio = int(request.POST.get("folio")) if request.POST.get("folio") else None
        demand.demander = demander
        demand.save()

        # save receiver email if not equal to user register email
        receiver_email = request.POST.get("receiver_email")
        if demander.mail != receiver_email:
            demander.receiver_mail = receiver_email
            demander.save()

        return JsonResponse({"msg": "success"})


def terminate_demand(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    demand_id = request.POST.get("demand_id")
    demand = Demand.objects.get(id=demand_id)
    demand.status = 1
    demand.save()

    return JsonResponse({"msg": "success"})


def delete_demand(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    demand_id = request.POST.get("demand_id")
    demand = Demand.objects.get(id=demand_id)
    demand.delete()

    return JsonResponse({"msg": "success"})

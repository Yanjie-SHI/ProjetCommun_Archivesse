from django.http import JsonResponse

from app01.models import *


def verify_login(request):
    options = {}
    login_user_id = request.session.get("login_user_id", 0)
    if login_user_id != 0:
        user = Users.objects.filter(id=login_user_id)
        if len(user) > 0:
            options.update({"user": user[0]})
    return options


def verify_login_js(request):
    login_user_id = request.session.get("login_user_id", 0)
    if login_user_id != 0:
        user = Users.objects.filter(id=login_user_id)
        if len(user) > 0:
            return JsonResponse({"msg": "success"})
        else:
            return JsonResponse({"msg": "fail"})
    else:
        return JsonResponse({"msg": "fail"})


def fetch_museum_address(request):
    options = {}
    museum_id = request.POST.get("museum_id")
    museum = Museum.objects.get(id=museum_id)
    options.update({"address": museum.address})
    options.update({"available_doc_archive_count": museum.document_limit})
    options.update({"available_video_archive_count": museum.video_limit})
    return JsonResponse(options)

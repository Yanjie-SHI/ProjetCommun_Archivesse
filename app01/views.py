from django.core.paginator import Paginator
from django.db.models import Q

from app01.utils import *
from web_historien import settings


# Create your views here.

def welcome(request):
    activate(settings.LANGUAGE_CODE)
    return render(request, 'welcome.html', {"lang": settings.LANGUAGE_CODE})


def to_search(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    if request.method == "GET":
        return render(request, 'search.html', options)


def search_archive(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # archive search
    input = request.POST.get("archiveKeyword")
    archive_search_type = request.POST.get("archiveSearchType")

    if archive_search_type == "2":
        archive_list = Archive.objects.filter(
            Q(Q(title__contains=input) | Q(description__contains=input)) & Q(type=1))
    elif archive_search_type == "3":
        archive_list = Archive.objects.filter(author__contains=input)
    else:
        archive_list = Archive.objects.filter(
            Q(title__contains=input) | Q(description__contains=input))

    options.update({"searchInput": input})
    options.update({"archiveSearchType": archive_search_type})
    # paginator
    archive_list_paginator = Paginator(archive_list, settings.PER_PAGE_SIZE)
    options.update({"archive_list": archive_list_paginator.get_page(current_page)})

    return render(request, "search_result_archive.html", options)


def search_archive_particles(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # archive search
    input = request.POST.get("archiveKeyword")
    search_particile = request.POST.get("particleRadios")
    archive_search_type = request.POST.get("archiveSearchType")
    # all words entered
    if search_particile == "1":
        if archive_search_type == "2":
            archive_list = Archive.objects.filter(
                Q(Q(title__contains=input) | Q(description__contains=input)) & Q(type=1))
        elif archive_search_type == "3":
            archive_list = Archive.objects.filter(author__contains=input)
        else:
            archive_list = Archive.objects.filter(Q(title__contains=input) | Q(description__contains=input))
    # at least one of the words entered
    elif search_particile == "2":
        input_split = input.split(" ")
        archive_list = []
        if archive_search_type == "2":
            for str in input_split:
                temp_archive_list = Archive.objects.filter(
                    Q(Q(title__contains=str) | Q(description__contains=str)) & Q(type=1))
                archive_list.append(temp_archive_list)
        elif archive_search_type == "3":
            for str in input_split:
                temp_archive_list = Archive.objects.filter(author__contains=str)
                archive_list.append(temp_archive_list)
        else:
            for str in input_split:
                temp_archive_list = Archive.objects.filter(
                    Q(title__contains=str) | Q(description__contains=str))
                archive_list.append(temp_archive_list)
    # exact expression
    elif search_particile == "3":
        if archive_search_type == "2":
            archive_list = Archive.objects.filter(Q(Q(title=input) | Q(description=input)) & Q(type__in=[2, 3]))
        elif archive_search_type == "3":
            archive_list = Archive.objects.filter(author=input)
        else:
            archive_list = Archive.objects.filter(Q(title=input) | Q(description=input))
    else:
        pass

    options.update({"particleRadios": search_particile})
    options.update({"search_input": input})
    options.update({"archiveSearchType": archive_search_type})
    # paginator
    archive_list_paginator = Paginator(archive_list, settings.PER_PAGE_SIZE)
    options.update({"archive_list": archive_list_paginator.get_page(current_page)})

    return render(request, "search_result_archive.html", options)


def search_resv(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # reservation search
    museum_name = request.POST.get("museumName")
    resv_end_date = request.POST.get("resvEndDate")
    archive_type = request.POST.get("archiveTypeRadios", "all")
    archive_count = request.POST.get("archive_count")
    current_page = request.POST.get("currentPage", "1")
    reservation_temp_list = []
    if resv_end_date:
        resv_end_date = datetime.date(int(resv_end_date[6:10]), int(resv_end_date[3:5]), int(resv_end_date[0:2]))
        # reservation search
        reservation_list = Reservation.objects.filter(
            Q(museum__name__contains=museum_name) & Q(expire_date__lte=resv_end_date) & Q(status=0))
    else:
        reservation_list = Reservation.objects.filter(status=0)
    for resv in reservation_list:
        resv.available_doc_archive_count = resv.museum.document_limit
        resv.available_video_archive_count = resv.museum.video_limit
        # recount available doc/video archive count, according to record numbers in Res_Dem_Arch table
        res_dem_arch = Res_Dem_Arch.objects.filter(reservation__id=resv.id)
        if len(res_dem_arch) > 0:
            for rda in res_dem_arch:
                if rda.archive.type == 0:
                    resv.available_doc_archive_count -= 1
                elif rda.archive.type == 2:
                    resv.available_video_archive_count -= 1
        # exclude search filter detail
        if archive_type == 'all':
            reservation_temp_list = reservation_list
        elif archive_type == "0" and archive_count and resv.available_doc_archive_count >= int(archive_count):
            reservation_temp_list.append(resv)
        elif archive_type == "2" and archive_count and resv.available_video_archive_count >= int(archive_count):
            reservation_temp_list.append(resv)

    options.update({"input_museum_name": museum_name})
    options.update({"input_archive_type": archive_type})
    options.update({"input_archive_count": archive_count})
    if resv_end_date:
        options.update({"input_resv_end_date": resv_end_date.strftime("%d/%m/%Y")})
    # paginator
    reservation_list_paginator = Paginator(reservation_temp_list, settings.PER_PAGE_SIZE)
    options.update({"reservation_list": reservation_list_paginator.get_page(current_page)})

    return render(request, "search_result_reservation.html", options)


def search_demand(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # demand search
    input = request.POST.get("demandSearchInput")
    demands = Demand.objects.filter(archive__id=input)
    options.update({"demandSearchInput": input})
    # paginator
    demands_list_paginator = Paginator(demands, settings.PER_PAGE_SIZE)
    options.update({"demands": demands_list_paginator.get_page(current_page)})

    return render(request, "search_result_demand.html", options)


def archive_detail(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    archive_id = request.GET.get("id") if request.GET.get("id") else request.POST.get("archive_id")
    archive = Archive.objects.filter(id=archive_id)
    if len(archive) > 0:
        options.update({"archive": archive[0]})
        # get favorite status
        if not request.session.get("login_user_id", 0) == 0:
            user_id = request.session["login_user_id"]
            favorites = Favorites.objects.filter(user__id=user_id, archive__id=archive_id)
            if len(favorites) > 0:
                options.update({"favorite_flag": "1"})
            else:
                options.update({"favorite_flag": "0"})
    return render(request, 'archive_detail.html', options)


def login(request):
    activate(settings.LANGUAGE_CODE)
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        options = {}
        options.update({"lang": settings.LANGUAGE_CODE})
        user = Users.objects.filter(mail=request.POST.get('email'), password=request.POST.get('password'))
        if len(user) > 0:
            request.session['login_user_id'] = user[0].id
            options.update({"user": user[0]})
            return render(request, 'search.html', options)
            # return render(request, 'search.html')
        else:
            return render(request, 'login.html', {"lang": settings.LANGUAGE_CODE})


def register(request):
    activate(settings.LANGUAGE_CODE)
    if request.method == "GET":
        options = {}
        options.update({"lang": settings.LANGUAGE_CODE})
        list_country = [
            {"key": "Germany", "display_name": "Allemagne"},
            {"key": "South Africa", "display_name": "Afrique du sud"},
            {"key": "Belgium", "display_name": "Belgique"},
            {"key": "China", "display_name": "Chine"},
            {"key": "United States", "display_name": "États-Unis"},
            {"key": "France", "display_name": "France"},
            {"key": "Greece", "display_name": "Grèce"}
        ]
        options.update({"list_data_init_country": list_country})
        return render(request, 'register.html', options)
    if request.method == "POST":
        # TODO verify password, if not equal to password, return Json response
        user = Users()
        user.mail = request.POST.get("email")
        user.first_name = request.POST.get("firstname")
        user.last_name = request.POST.get("lastname")
        user.username = user.first_name + " " + user.last_name.upper()
        user.password = request.POST.get("password")
        user.gender = int(request.POST.get("genderRadios"))
        user.nation = request.POST.get("pays")
        # user.address = request.POST.get("address")
        if request.POST.get("post_code"):
            user.post_code = int(request.POST.get("post_code"))
        user.save()

        return render(request, 'login.html', {"lang": settings.LANGUAGE_CODE})


def self_center(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    if not options.get("user", ""):
        return render(request, "login.html")
    if request.method == "GET":
        user_id = request.session['login_user_id']
        user = Users.objects.get(id=user_id)
        if user:
            options.update({"user": user})
            return render(request, 'self_center.html', options)
    elif request.method == "POST":
        return render(request, 'self_center.html')


def message_list(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    message_list = Notification.objects.filter(receiver=options.get("user"))
    options.update({"message_list": message_list})

    return render(request, 'my_messages.html', options)


def message_detail(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    message = Notification.objects.get(id=request.GET.get("id"))
    message.status = 1
    message.save()
    options.update({"message": message})

    return render(request, 'message_detail.html', options)


def fetch_my_mew_message_for_header_icon(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) != 0:
        options = verify_login(request)
        new_messages = Notification.objects.filter(receiver=options.get("user"), status=0)
        if len(new_messages) > 0:
            return JsonResponse({"msg": True})
        else:
            return JsonResponse({"msg": False})
    else:
        return JsonResponse({"msg": False})


def profile(request):
    activate(settings.LANGUAGE_CODE)
    options = verify_login(request)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    user_id = request.session['login_user_id']
    user = Users.objects.get(id=user_id)
    if request.method == "GET":
        if user:
            options.update({"user": user})
        return render(request, 'my_profile.html', options)
    elif request.method == "POST":
        if user:
            if request.POST['old_password'] and not request.POST['old_password'] == user.password:
                return JsonResponse({"err": "old password input error"})
            user.gender = request.POST['genderRadios']
            user.nation = request.POST['nation']
            user.post_code = request.POST['post_code']
            user.city = request.POST['city']
            user.address = request.POST['address']
            user.password = request.POST['new_password']
            user.save()
        return JsonResponse({"msg": "success"})


def favorites(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    current_page = request.POST.get("currentPage", "1")
    favorites = Favorites.objects.filter(user=options.get("user"))
    favorites_paginator = Paginator(favorites, settings.PER_PAGE_SIZE)
    options.update({"favorite_list": favorites_paginator.get_page(current_page)})

    return render(request, 'my_favorites.html', options)


def add_favorites(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    if request.method == "POST":
        user_id = request.session["login_user_id"]
        archive_id = request.POST.get("archive_id")

        favorites = Favorites()
        favorites.user_id = user_id
        favorites.archive_id = archive_id
        favorites.save()

        return archive_detail(request)


def remove_favorites(request):
    activate(settings.LANGUAGE_CODE)
    if request.method == "POST":
        user_id = request.session["login_user_id"]
        archive_id = request.POST.get("archive_id")

        favorites = Favorites.objects.filter(user__id=user_id, archive__id=archive_id)
        if len(favorites) > 0:
            favorites.delete()

        request.POST.archive_id = archive_id
        return archive_detail(request)


def logout(request):
    activate(settings.LANGUAGE_CODE)
    request.session.clear()
    return render(request, 'search.html')

import datetime

from django.db.models import Q
from django.shortcuts import render

from app01.utils import *
from web_historien import settings


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def to_search(request):
    options = verify_login(request)
    if request.method == "GET":
        return render(request, 'search.html', options)


def search_archive(request):
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
    options.update({"total_size": len(archive_list)})
    total_pages = int(len(archive_list) / settings.PER_PAGE_SIZE) + 1
    pages = []
    for page in range(1, total_pages + 1, 1):
        pages.append(page)
    options.update({"pages": pages})
    options.update({"current_page": current_page})
    options.update({"search_input": input})
    options.update({"archive_search_type": archive_search_type})
    options.update({"archive_list": archive_list})

    return render(request, "search_result_archive.html", options)


def search_resv(request):
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # reservation search
    museum_name = request.POST.get("museumName")
    resv_end_date = request.POST.get("resvEndDate")
    resv_end_date = datetime.date(int(resv_end_date[6:10]), int(resv_end_date[3:5]), int(resv_end_date[0:2]))

    current_page = request.POST.get("currentPage", "1")
    # reservation search
    reservation_list = Reservation.objects.filter(
        Q(museum__name__contains=museum_name) & Q(expire_date__lte=resv_end_date))
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

    options.update({"total_size": len(reservation_list)})
    total_pages = int(len(reservation_list) / settings.PER_PAGE_SIZE) + 1
    pages = []
    for page in range(1, total_pages + 1, 1):
        pages.append(page)
    options.update({"pages": pages})
    options.update({"current_page": current_page})
    options.update({"input_museum_name": museum_name})
    options.update({"input_resv_end_date": resv_end_date.strftime("%d/%m/%Y")})
    options.update({"reservation_list": reservation_list})

    return render(request, "search_result_reservation.html", options)


def search_demand(request):
    options = verify_login(request)
    current_page = request.POST.get("currentPage", "1")
    # demand search
    input = request.POST.get("demandSearchInput")
    demands = Demand.objects.filter(archive__id=input)
    options.update({"demands": demands})

    return render(request, "search_result_demand.html", options)


def archive_detail(request):
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
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        options = {}
        user = Users.objects.filter(mail=request.POST.get('email'), password=request.POST.get('password'))
        if len(user) > 0:
            request.session['login_user_id'] = user[0].id
            options.update({"user": user[0]})
            return render(request, 'search.html', options)
            # return render(request, 'search.html')
        else:
            return render(request, 'login.html')


def register(request):
    if request.method == "GET":
        options = {}
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
        user.address = request.POST.get("address")
        user.post_code = request.POST.get("post_code")
        user.save()

        return render(request, 'login.html')


def self_center(request):
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
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    return render(request, 'my_messages.html')


def profile(request):
    options = verify_login(request)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    user_id = request.session['login_user_id']
    user = Users.objects.get(u_id=user_id)
    if request.method == "GET":
        if user:
            options.update({"user": user})
        return render(request, 'my_profile.html', options)
    elif request.method == "POST":
        if user:
            if request.POST['old_password'] and not request.POST['old_password'] == user.u_password:
                return JsonResponse({"err": "old password input error"})
            user.u_gender = request.POST['genderRadios']
            user.u_nation = request.POST['nation']
            user.u_post_code = request.POST['post_code']
            user.u_city = request.POST['city']
            user.u_address = request.POST['address']
            user.u_password = request.POST['new_password']
            user.save()
        return JsonResponse({"msg": "User update success!"})


def favorites(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    return render(request, 'my_favorites.html')


def add_favorites(request):
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
    if request.method == "POST":
        user_id = request.session["login_user_id"]
        archive_id = request.POST.get("archive_id")

        favorites = Favorites.objects.filter(user__id=user_id, archive__id=archive_id)
        if len(favorites) > 0:
            favorites.delete()

        request.POST.archive_id = archive_id
        return archive_detail(request)


def logout(request):
    request.session.clear()
    return render(request, 'search.html')

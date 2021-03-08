import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from app01.models import Users, Archive, Reservation
from web_historien import settings


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def search(request):
    if request.method == "GET":
        options = {}
        return render(request, 'search.html', options)
    elif request.method == "POST":
        input = request.POST.get("searchInput")
        current_page = request.POST.get("currentPage", "1")
        # archive search
        if request.POST.get("searchType") == "1":
            search_particile = request.POST.get("particleRadios")
            archive_search_type = request.POST.get("archiveSearchType")
            # all words entered
            if search_particile == "1":
                if archive_search_type == "2":
                    archive_list = Archive.objects.filter(
                        Q(Q(title__contains=input) | Q(description__contains=input)) & Q(type__in=[2, 3]))
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
                            Q(Q(title__contains=str) | Q(description__contains=str)) & Q(type__in=[2, 3]))
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

            options = {}
            options.update({"particleRadios": search_particile})
            options.update({"total_size": len(archive_list)})
            total_pages = int(len(archive_list) / settings.PER_PAGE_SIZE) + 1
            pages = []
            for page in range(1, total_pages + 1, 1):
                pages.append(page)
            options.update({"pages": pages})
            options.update({"current_page": current_page})
            options.update({"search_input": input})
            options.update({"archive_list": archive_list})

            return render(request, "search_result_archive.html", options)
        # reservation search
        elif request.POST.get("searchType") == "2":
            museum_name = request.POST.get("museumName")
            resv_end_date = request.POST.get("resvEndDate")
            resv_end_date = datetime.date(int(resv_end_date[0:4]), int(resv_end_date[5:7]), int(resv_end_date[8:10]))

            current_page = request.POST.get("currentPage", "1")
            # reservation search
            reservation_list = Reservation.objects.filter(museum__name=museum_name, expire_date__lte=resv_end_date)

            options = {}
            options.update({"total_size": len(reservation_list)})
            total_pages = int(len(reservation_list) / settings.PER_PAGE_SIZE) + 1
            pages = []
            for page in range(1, total_pages + 1, 1):
                pages.append(page)
            options.update({"pages": pages})
            options.update({"current_page": current_page})
            options.update({"search_input": input})
            options.update({"reservation_list": reservation_list})

            return render(request, "search_result_reservation.html", options)
        # demand search
        elif request.POST.get("searchType") == "3":
            pass
        else:
            pass


def archive_detail(request):
    if request.method == "GET":
        archive_id = request.GET.get("id")
        archive = Archive.objects.filter(id=archive_id)
        options = {}
        if len(archive) > 0:
            options.update({"archive": archive[0]})
            return render(request, 'archive_detail.html', options)
    elif request.method == "POST":
        # save star to favorites
        pass


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        options = {}
        user = Users.objects.filter(u_mail=request.POST.get('email'), u_password=request.POST.get('password'))
        if len(user) > 0:
            request.session['login_user_id'] = user[0].u_id
            options.update({"user": user[0]})
            return render(request, 'search.html', options)
            # return render(request, 'search.html')
        else:
            return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def self_center(request):
    if request.method == "GET":
        options = {}
        user_id = request.session['login_user_id']
        user = Users.objects.get(u_id=user_id)
        if user:
            options.update({"user": user})
            return render(request, 'self_center.html', options)
    elif request.method == "POST":
        return render(request, 'self_center.html')


def message_list(request):
    if not request.session["login_user_id"]:
        return render(request, "login.html")
    return render(request, 'message_list.html')


def profile(request):
    user_id = request.session['login_user_id']
    user = Users.objects.get(u_id=user_id)
    if request.method == "GET":
        options = {}
        if user:
            options.update({"user": user})
        return render(request, 'profile.html', options)
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
    if not request.session["login_user_id"]:
        return render(request, "login.html")
    return render(request, 'favorites.html')


def add_favorites(request):
    if request.method == "POST":
        user_id = request.session["login_user_id"]
        archive_id = request.POST.get("archive_id")

        # TODO

        return JsonResponse({"msg": "Add to favorites success!"})


def reservation(request):
    if not request.session["login_user_id"]:
        return render(request, "login.html")
    return render(request, 'reservation.html')


def logout(request):
    request.session.clear()
    return render(request, 'search.html')

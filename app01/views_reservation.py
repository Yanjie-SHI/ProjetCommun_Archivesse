import datetime

from django.db.models import Q
from django.shortcuts import render

from app01.utils import *


# Create your views here.


def to_my_reservation_list(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")

    options = verify_login(request)
    # get all my related reservation
    result_set = set()
    # find all reservation as creator
    reservation_list = Reservation.objects.filter(creator=options.get("user"))
    if len(reservation_list) > 0:
        for resv in reservation_list:
            result_set.add(resv)
    # find all reservation as joiner
    res_dem_arch_resvid_list = Res_Dem_Arch.objects.filter(resv_user=options.get("user")).values("reservation_id")
    reservation_list2 = Reservation.objects.filter(id__in=res_dem_arch_resvid_list)
    if len(reservation_list2) > 0:
        for resv in reservation_list2:
            result_set.add(resv)

    # get all corresponding archive for each reservation
    for resv in result_set:
        archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv.id, resv_user=options.get("user"))
        resv.archive_list = archive_list

    options.update({"reservation_list": result_set})

    return render(request, 'my_reservation.html', options)


def to_resv_detail_creatorview(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")

    options = verify_login(request)

    resv_id = request.GET.get("resv_id")
    resv = Reservation.objects.get(id=resv_id)

    resv_users_list = Res_Dem_Arch.objects.filter(
        Q(reservation__id=resv_id) & ~Q(resv_user=options.get("user"))).values_list("resv_user_id",
                                                                                    flat=True).distinct()
    doc_archive_lists = []
    video_archive_lists = []
    count_doc_archive_exclude_my = 0
    count_video_archive_exclude_my = 0
    for user_id in resv_users_list:
        doc_archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv_id, archive__type=0, resv_user__id=user_id)
        if len(doc_archive_list) > 0:
            user_doc_archive_list = {"user": Users.objects.get(id=user_id), "doc_archive_list": doc_archive_list}
            doc_archive_lists.append(user_doc_archive_list)
            count_doc_archive_exclude_my += len(doc_archive_list)
        video_archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv_id, archive__type=2,
                                                         resv_user__id=user_id)
        if len(video_archive_list) > 0:
            user_video_archive_list = {"user": Users.objects.get(id=user_id), "video_archive_list": video_archive_list}
            video_archive_lists.append(user_video_archive_list)
            count_video_archive_exclude_my += len(video_archive_list)
    resv.count_doc_archive_exclude_my = count_doc_archive_exclude_my
    resv.count_video_archive_exclude_my = count_video_archive_exclude_my
    resv.doc_archive_lists = doc_archive_lists
    resv.video_archive_lists = video_archive_lists
    options.update({"reservation": resv})

    return render(request, "reservation_detail_creatorview.html", options)


def to_create_reservation(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    if request.method == "GET":
        return render(request, "create_reservation.html", options)
    elif request.method == "POST":
        museum_list = Museum.objects.all()
        options.update({"museum_list": museum_list})

        input_museum_name = request.POST.get("museumName")
        input_resv_end_date = request.POST.get("resvEndDate")
        options.update({"museum_name": input_museum_name})
        options.update({"resv_end_date": input_resv_end_date})

        museum = Museum.objects.filter(name__contains=input_museum_name)
        if len(museum) > 0:
            available_doc_archive_count = museum[0].document_limit
            available_video_archive_count = museum[0].video_limit
            options.update({"available_doc_archive_count": available_doc_archive_count})
            options.update({"available_video_archive_count": available_video_archive_count})

        return render(request, "reservation_create.html", options)


def create_reservation(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    if request.method == "POST":
        # save data in Reservation
        reservation = Reservation()
        resv_end_date = request.POST.get("resvEndDate")
        resv_end_date = datetime.date(int(resv_end_date[6:10]), int(resv_end_date[3:5]), int(resv_end_date[0:2]))
        reservation.expire_date = resv_end_date
        reservation.status = 0
        reservation.sent_flag = 0
        reservation.received_flag = 0
        reservation.museum_id = int(request.POST.get("sel_museum"))
        reservation.creator_id = int(request.session.get("login_user_id"))
        reservation.save()

        # save data in relation Res_Dem_Arch
        resv_id = reservation.id
        demand_user = options.get("user")
        needed_doc_demand_count = request.POST.get("needed_doc_demand_count")
        needed_video_demand_count = request.POST.get("needed_video_demand_count")

        for i in range(1, int(needed_doc_demand_count) + 1):
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("doc_archive_id_" + str(i))
            if request.POST.get("doc_folio_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("doc_folio_" + str(i)))
            res_dem_arch.save()

        for i in range(1, int(needed_video_demand_count) + 1):
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("video_archive_id_" + str(i))
            if request.POST.get("video_ouvert_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("video_ouvert_" + str(i)))
            res_dem_arch.save()

        # save receiver email if not equal to user register email
        receiver_email = request.POST.get("receiver_email")
        if demand_user.mail != receiver_email:
            demand_user.receiver_mail = receiver_email
            demand_user.save()

        return JsonResponse({"msg": "success"})


def join_reservation(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)
    if request.method == "GET":
        resv_id = request.GET.get("id")
        reservation = Reservation.objects.filter(id=resv_id)
        if len(reservation) > 0:
            options.update({"reservation": reservation[0]})

            # get available document archive count
            available_doc_archive_count = reservation[0].museum.document_limit
            # get available video archive count
            available_video_archive_count = reservation[0].museum.video_limit
            # recount available doc/video archive count, according to record numbers in Res_Dem_Arch table
            res_dem_arch = Res_Dem_Arch.objects.filter(reservation__id=resv_id)
            if len(res_dem_arch) > 0:
                for rda in res_dem_arch:
                    if rda.archive.type == 0:
                        available_doc_archive_count -= 1
                    elif rda.archive.type == 2:
                        available_video_archive_count -= 1

            options.update({"available_doc_archive_count": available_doc_archive_count})
            options.update({"available_video_archive_count": available_video_archive_count})

            return render(request, "reservation_detail_join.html", options)
    elif request.method == "POST":
        # save data in relation Res_Dem_Arch
        resv_id = request.POST.get("resv_id")
        demand_user = options.get("user")
        needed_doc_demand_count = request.POST.get("needed_doc_demand_count")
        needed_video_demand_count = request.POST.get("needed_video_demand_count")

        for i in range(1, int(needed_doc_demand_count) + 1):
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("doc_archive_id_" + str(i))
            if request.POST.get("doc_folio_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("doc_folio_" + str(i)))
            res_dem_arch.save()

        for i in range(1, int(needed_video_demand_count) + 1):
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("video_archive_id_" + str(i))
            if request.POST.get("video_ouvert_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("video_ouvert_" + str(i)))
            res_dem_arch.save()

        # save receiver email if not equal to user register email
        receiver_email = request.POST.get("receiver_email")
        if demand_user.mail != receiver_email:
            demand_user.receiver_mail = receiver_email
            demand_user.save()

        return JsonResponse({"msg": "success"})


def undo_join_reservation(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    resv_id = request.POST.get("resv_id")
    res_dem_arch = Res_Dem_Arch.objects.filter(reservation__id=resv_id, resv_user=options.get("user"))
    for record in res_dem_arch:
        record.delete()

    return JsonResponse({"msg": "success"})


def confirm_sent_receive_status(request):
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    resv_id = request.POST.get("resv_id")
    # demander confirm all archives received
    res_dem_confirm_status = Res_Dem_Confirm_Status()
    res_dem_confirm_status.reservation_id = int(resv_id)
    res_dem_confirm_status.resv_user = options.get("user")
    res_dem_confirm_status.received_flag = 1
    res_dem_confirm_status.save()

    return JsonResponse({"msg": "success"})

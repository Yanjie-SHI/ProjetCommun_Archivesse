from django.db.models import Q

from app01.utils import *


# Create your views here.


def to_my_reservation_list(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")

    options = verify_login(request)
    # get all my related reservation
    result_set = set()
    # find all reservation as creator
    reservation_list = Reservation.objects.filter(creator=options.get("user"), status__lt=2)
    if len(reservation_list) > 0:
        for resv in reservation_list:
            result_set.add(resv)
    # find all reservation as joiner
    res_dem_arch_resvid_list = Res_Dem_Arch.objects.filter(resv_user=options.get("user")).values("reservation_id")
    reservation_list2 = Reservation.objects.filter(id__in=res_dem_arch_resvid_list, status__lt=2)
    if len(reservation_list2) > 0:
        for resv in reservation_list2:
            result_set.add(resv)
    # get all corresponding archive for each reservation
    for resv in result_set:
        archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv.id, resv_user=options.get("user"))
        resv.archive_list = archive_list

    options.update({"reservation_list": result_set})

    # get all finished reservations
    result_set_finished = set()
    # find all reservation as creator
    reservation_list_finished = Reservation.objects.filter(creator=options.get("user"), status=2)
    if len(reservation_list_finished) > 0:
        for resv in reservation_list_finished:
            result_set_finished.add(resv)
    # find all reservation as joiner
    res_dem_arch_resvid_finished_list = Res_Dem_Arch.objects.filter(resv_user=options.get("user"),
                                                                    reservation__status=2).values("reservation_id")
    reservation_list_finished2 = Reservation.objects.filter(id__in=res_dem_arch_resvid_finished_list)
    if len(reservation_list_finished2) > 0:
        for resv in reservation_list_finished2:
            result_set_finished.add(resv)
    # get all corresponding archive for each reservation
    for resv in result_set_finished:
        archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv.id, resv_user=options.get("user"))
        resv.archive_list = archive_list

    options.update({"reservation_list_finished": result_set_finished})

    return render(request, 'my_reservation.html', options)


def to_resv_detail_creatorview(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")

    options = verify_login(request)

    resv_id = request.GET.get("resv_id")
    resv = Reservation.objects.get(id=resv_id)

    resv_users_list = Res_Dem_Arch.objects.filter(
        Q(reservation__id=resv_id) & ~Q(resv_user=options.get("user"))).values_list("resv_user_id",
                                                                                    flat=True).distinct()
    resv_doc_archive_lists = []
    resv_video_archive_lists = []
    count_doc_archive_exclude_my = 0
    count_video_archive_exclude_my = 0
    for user_id in resv_users_list:
        doc_archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv_id, archive__type=0, resv_user__id=user_id)
        if len(doc_archive_list) > 0:
            sent_flag = Res_Dem_Confirm_Status.objects.get(reservation__id=resv_id, resv_user__id=user_id,
                                                           arch_type=0).sent_flag
            user_doc_archive_list = {"user": Users.objects.get(id=user_id), "doc_archive_list": doc_archive_list,
                                     "sent_flag": sent_flag}
            resv_doc_archive_lists.append(user_doc_archive_list)
            count_doc_archive_exclude_my += len(doc_archive_list)
        video_archive_list = Res_Dem_Arch.objects.filter(reservation__id=resv_id, archive__type=2,
                                                         resv_user__id=user_id)
        if len(video_archive_list) > 0:
            sent_flag = Res_Dem_Confirm_Status.objects.get(reservation__id=resv_id, resv_user__id=user_id,
                                                           arch_type=2).sent_flag
            user_video_archive_list = {"user": Users.objects.get(id=user_id), "video_archive_list": video_archive_list,
                                       "sent_flag": sent_flag}
            resv_video_archive_lists.append(user_video_archive_list)
            count_video_archive_exclude_my += len(video_archive_list)
    resv.count_doc_archive_exclude_my = count_doc_archive_exclude_my
    resv.count_video_archive_exclude_my = count_video_archive_exclude_my
    resv.doc_archive_lists = resv_doc_archive_lists
    resv.video_archive_lists = resv_video_archive_lists
    options.update({"reservation": resv})

    return render(request, "reservation_detail_creatorview.html", options)


def to_create_reservation(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    museum_list = Museum.objects.all()
    options.update({"museum_list": museum_list})

    input_museum_name = request.POST.get("museumName", "")
    input_resv_end_date = request.POST.get("resvEndDate", "")
    options.update({"museum_name": input_museum_name})
    options.update({"resv_end_date": input_resv_end_date})

    if input_museum_name:
        museum = Museum.objects.filter(name__contains=input_museum_name)
        if len(museum) > 0:
            options.update({"address": museum[0].address})
            options.update({"available_doc_archive_count": museum[0].document_limit})
            options.update({"available_video_archive_count": museum[0].video_limit})
    else:
        options.update({"address": museum_list[0].address})
        options.update({"resv_end_date": datetime.datetime.today()})
        options.update({"available_doc_archive_count": museum_list[0].document_limit})
        options.update({"available_video_archive_count": museum_list[0].video_limit})

    return render(request, "reservation_create.html", options)


def create_reservation(request):
    activate(settings.LANGUAGE_CODE)
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
        reservation.creator = options.get("user")
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

        # save a message data in Message table
        notification = Notification()
        notification.category = 1
        notification.title = "Confirmation de création de rendez-vous"
        notification.content = "Bonjour,</br></br>&nbsp;&nbsp;&nbsp;&nbsp;Vous avez crée le rendez-vous à {} avec succès.</br></br></br>Cordialement,</br>Groupe Archivesse".format(
            reservation.museum.name)
        notification.status = 0
        notification.create_date_time = datetime.datetime.now()
        notification.receiver = options.get("user")
        notification.save()

        return JsonResponse({"msg": "success"})


def join_reservation(request):
    activate(settings.LANGUAGE_CODE)
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
            # save data in Res_Dem_Arch relation
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("doc_archive_id_" + str(i))
            if request.POST.get("doc_folio_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("doc_folio_" + str(i)))
            res_dem_arch.save()
        # save data in Res_Dem_Confirm_Status relation
        if int(needed_doc_demand_count) > 0:
            res_dem_confirm_status = Res_Dem_Confirm_Status()
            res_dem_confirm_status.reservation_id = resv_id
            res_dem_confirm_status.resv_user = options.get("user")
            res_dem_confirm_status.arch_type = 0
            res_dem_confirm_status.sent_flag = 0
            res_dem_confirm_status.received_flag = 0
            res_dem_confirm_status.save()

        for i in range(1, int(needed_video_demand_count) + 1):
            res_dem_arch = Res_Dem_Arch()
            res_dem_arch.reservation_id = int(resv_id)
            res_dem_arch.resv_user_id = demand_user.id
            res_dem_arch.archive_id = request.POST.get("video_archive_id_" + str(i))
            if request.POST.get("video_ouvert_" + str(i)):
                res_dem_arch.folio = int(request.POST.get("video_ouvert_" + str(i)))
            res_dem_arch.save()
        # save data in Res_Dem_Confirm_Status relation
        if int(needed_video_demand_count) > 0:
            res_dem_confirm_status = Res_Dem_Confirm_Status()
            res_dem_confirm_status.reservation_id = resv_id
            res_dem_confirm_status.resv_user = options.get("user")
            res_dem_confirm_status.arch_type = 2
            res_dem_confirm_status.sent_flag = 0
            res_dem_confirm_status.received_flag = 0
            res_dem_confirm_status.save()

        # save receiver email if not equal to user register email
        receiver_email = request.POST.get("receiver_email")
        if (demand_user.receiver_mail and demand_user.receiver_mail != receiver_email) or (
                not demand_user.receiver_mail and demand_user.mail != receiver_email):
            demand_user.receiver_mail = receiver_email
            demand_user.save()

        return JsonResponse({"msg": "success"})


def undo_join_reservation(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    # delete data in Res_Dem_Arch
    resv_id = request.POST.get("resv_id")
    res_dem_arch = Res_Dem_Arch.objects.filter(reservation__id=resv_id, resv_user=options.get("user"))
    for record in res_dem_arch:
        record.delete()

    # delete data from Res_Dem_Confirm_Status
    res_dem_confirm_status = Res_Dem_Confirm_Status.objects.filter(reservation__id=resv_id,
                                                                   resv_user=options.get("user"))
    for record in res_dem_confirm_status:
        record.delete()

    return JsonResponse({"msg": "success"})


def confirm_sent_receive_status(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    resv_id = request.POST.get("resv_id")
    resv = Reservation.objects.get(id=resv_id)
    if resv.creator == options.get("user"):
        # creator update sent status
        receiver_id = request.POST.get("receiver_id")
        receiver = Users.objects.get(id=receiver_id)
        arch_type = request.POST.get("arch_type")
        res_dem_confirm_status = Res_Dem_Confirm_Status.objects.filter(reservation__id=resv_id, resv_user=receiver,
                                                                       arch_type=arch_type)
        if len(res_dem_confirm_status) > 0:
            res_dem_confirm_status[0].sent_flag = 1
            res_dem_confirm_status[0].save()

        return JsonResponse({"msg": "success"})
    else:
        # demander confirm all archives received, both archive type = 0 and 2
        res_dem_confirm_status = Res_Dem_Confirm_Status.objects.filter(reservation__id=resv_id,
                                                                       resv_user=options.get("user"))
        for record in res_dem_confirm_status:
            record.received_flag = 1
            record.save()
        return JsonResponse({"msg": "success"})


def update_resv_status(request):
    activate(settings.LANGUAGE_CODE)
    if request.session.get("login_user_id", 0) == 0:
        return render(request, "login.html")
    options = verify_login(request)

    resv_id = request.POST.get("resv_id")
    status = request.POST.get("status")

    reservation = Reservation.objects.get(id=resv_id)
    if status == "1":
        reservation.status = "1"
        reservation.save()
    elif status == "0":
        reservation.status = "0"
        reservation.save()

    return JsonResponse({"msg": "success"})

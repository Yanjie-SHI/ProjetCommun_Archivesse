from app01.models import *
from app01.utils import create_message


def update_resv_status():
    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    reservations = Reservation.objects.all()
    count_updated = 0
    for resv in reservations:
        resv_dem_confirm_status = Res_Dem_Confirm_Status.objects.filter(reservation__id=resv.id)
        confirm_status_size = len(resv_dem_confirm_status)
        count_double_confirmed = 0
        if confirm_status_size > 0:
            for record in resv_dem_confirm_status:
                if record.sent_flag == 1 and record.received_flag == 1:
                    count_double_confirmed += 1
            if confirm_status_size == count_double_confirmed:
                if resv.status == 1:
                    resv.status = 2
                    resv.save()
                    count_updated += 1
                    print(now + " - Reservation {} status updated to 2(finished).".format(str(resv.id)))
                    # save a message data in Message table
                    content = "Le rendez-vous N° {} à {} est terminé avec succès.".format(resv.id, resv.museum.name)
                    create_message(1, "Confirmation de finalisation de rendez-vous", content, resv.creator)
    if count_updated == 0:
        print(now + " - Nothing to be updated.")

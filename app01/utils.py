from app01.models import *


def verify_login(request):
    options = {}
    login_user_id = request.session.get("login_user_id", 0)
    if login_user_id != 0:
        user = Users.objects.filter(id=login_user_id)
        if len(user) > 0:
            options.update({"user": user[0]})
    return options

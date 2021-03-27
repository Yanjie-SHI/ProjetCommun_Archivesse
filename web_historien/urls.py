"""web_historien URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app01 import views, views_reservation as views_resv, views_demand, utils

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.welcome),
    url(r'^to_search', views.to_search),
    url(r'^search_archive', views.search_archive),
    url(r'^search_resv', views.search_resv),
    url(r'^search_demand', views.search_demand),
    url(r'^archive_detail', views.archive_detail),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^selfcenter', views.self_center),
    url(r'^messagelist', views.message_list),
    url(r'^message_detail', views.message_detail),
    url(r'^profile', views.profile),
    url(r'^favorites', views.favorites),
    url(r'^add_favorites', views.add_favorites),
    url(r'^remove_favorites', views.remove_favorites),
    url(r'^logout', views.logout),

    url(r'^to_my_reservation', views_resv.to_my_reservation_list),
    url(r'^to_resv_detail_creatorview', views_resv.to_resv_detail_creatorview),
    url(r'^to_create_resv', views_resv.to_create_reservation),
    url(r'^create_resv', views_resv.create_reservation),
    url(r'^join_resv', views_resv.join_reservation),
    url(r'^undo_join_resv', views_resv.undo_join_reservation),
    url(r'^confirm_sent_receive_status', views_resv.confirm_sent_receive_status),
    url(r'^update_resv_status', views_resv.update_resv_status),

    url(r'^to_my_demand', views_demand.to_my_demand),
    url(r'^to_create_demand', views_demand.to_create_demand),
    url(r'^create_demand', views_demand.create_demand),
    url(r'^terminate_demand', views_demand.terminate_demand),
    url(r'^delete_demand', views_demand.delete_demand),

    url(r'^fetchmuseumaddress', utils.fetch_museum_address),
    url(r'^fetchmuseumname', utils.fetch_museum_name),
    url(r'^verify_login', utils.verify_login_js),
    url(r'change_language', utils.change_language),

]

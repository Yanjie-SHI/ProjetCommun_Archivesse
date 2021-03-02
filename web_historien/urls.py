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

from app01 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.welcome),
    url(r'^search/', views.search),
    url(r'^searchresult', views.search_result),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^selfcenter', views.self_center),
    url(r'^messagelist', views.message_list),
    url(r'^profile', views.profile),
    url(r'^favorites', views.favorites),
    url(r'^reservation', views.reservation),
    url(r'^logout', views.logout),
]

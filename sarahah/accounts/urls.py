from django.conf.urls import url, include
from django.contrib import admin

<<<<<<< HEAD

from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path

from .views import dashboard, register, settings, editProfile, changePassword, removeProfile, ActivateAccount

app_name = "accounts"
urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^login/$',   LoginView.as_view(
            template_name='accounts/login.html'
        ), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
=======
from django.contrib.auth import login, logout


from .views import dashboard, register, settings, editProfile, changePassword, removeProfile

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page':'core:home'}, name="logout"),
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827
    url(r'^register/', register, name="register"),
    url(r'^settings/(?P<setting>[\w]+)/', settings, name="settings"),

    url(r'^edit/', editProfile, name="editProfile"),
    url(r'^cgdPassword/', changePassword, name="changePassword"),
    url(r'^rmvProfile/', removeProfile, name="removeProfile"),
<<<<<<< HEAD
    path('activate/<uidb64>/<token>/',
             ActivateAccount.as_view(), name='activate'),
=======
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827
]

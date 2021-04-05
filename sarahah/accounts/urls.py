from django.conf.urls import url, include
from django.contrib import admin


from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path

from .views import dashboard, register, settings, editProfile, changePassword, removeProfile, ActivateAccount, terms

app_name = "accounts"
urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^login/terms/$', terms, name="terms"),
    url(r'^login/$',   LoginView.as_view(
            template_name='accounts/login.html'
        ), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/', register, name="register"),
    url(r'^settings/(?P<setting>[\w]+)/', settings, name="settings"),

    url(r'^edit/', editProfile, name="editProfile"),
    url(r'^cgdPassword/', changePassword, name="changePassword"),
    url(r'^rmvProfile/', removeProfile, name="removeProfile"),
    # path('activate/<uidb64>/<token>/',
    #          ActivateAccount.as_view(), name='activate'),
]

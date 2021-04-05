from django.conf.urls import url, include

from .views import favoriteMessage, deleteMessage, reportMessage


urlpatterns = [
    url(r'favorite/(?P<idMessage>[\w0-9_-]+)/', favoriteMessage, name='favorite'),
    url(r'delete/(?P<idMessage>[\w0-9_-]+)/', deleteMessage, name='delete'),
    url(r'report/(?P<idMessage>[\w0-9_-]+)/', reportMessage, name='report'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^(?P<state>[a-z]+)/(?P<keyword>[a-z]+)$', views.index, name='index'),
    url(r'^(?P<state>[a-z]+)/(?P<session>[a-zA-Z0-9-_ ]+)/(?P<bill_id>[a-zA-Z0-9% ]+)/$', views.detail, name='detail')
]
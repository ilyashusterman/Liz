from django.conf.urls import url
from django.conf import settings
from django.views.static import  serve
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^add_trip/$', views.add_trip, name='add_trip'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
from django.conf.urls import url
from django.conf import settings
from django.views.static import  serve
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^add_trip/$', views.add_trip, name='add_trip'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^like_trip/$', views.like_trip, name='like_trip'),
    url(r'^sales/$', views.sales, name='sales'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
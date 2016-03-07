from django.conf.urls import patterns, url
from registeration import views
from .views import (EventDetailView,EventUserRegisterView)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^events/$', views.events, name='events'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^user_register/$', views.user_register, name='user_register'),
    url(r'^user_deregister/$', views.user_deregister, name='user_deregister'),

    url(
        r'^events/$',views.listview,
        name="events_event_list"
    ),
    url(
        r'^(?P<pk>\d+)/$',
        EventDetailView.as_view(),
        name="events_event_detail"
    ),
    url(
        (r'^register/(?P<event_id>\d+)/user/$'),
        EventUserRegisterView.as_view(),
        name="events_event_user_registration"
    ),
)
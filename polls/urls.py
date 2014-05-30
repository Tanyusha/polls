# coding=utf-8
__author__ = 'Таника'

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='poll_index'),
    url(r'^add/$', views.add_poll, name='add_poll'),
    url(r'^(?P<poll_id>\d+)/add_choice/$', views.add_choice, name='add_choice'),
    url(r'^(?P<poll_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<poll_id>\d+)/poll_del/$', views.poll_delete, name='poll_del'),
    url(r'^(?P<poll_id>\d+)/choice_del/(?P<choice_id>\d+)/$', views.choice_delete, name='choice_del'),
    url(r'^del_message/$', views.del_message, name='del_message'),
    url(r'^(?P<poll_id>\d+)/send/$', views.send, name='send'),
    url(r'^(?P<recv_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<recv_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<poll_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/results/votes_details/$', views.votes_details, name='votes_details'),
)
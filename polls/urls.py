# coding=utf-8
__author__ = 'Таника'

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='poll_index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^add_poll/', views.add_poll, name='add_poll'),
    url(r'^add_choice/', views.add_choice, name='add_choice'),
)
# coding=utf-8
__author__ = 'Таника'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
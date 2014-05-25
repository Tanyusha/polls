# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from auth.urls import urlpatterns as auth_urlpatterns

import registration.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^registration/', registration.views.register, name='registration'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += auth_urlpatterns


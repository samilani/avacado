from django.conf.urls import patterns, url
from idea import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
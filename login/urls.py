from django.conf.urls import patterns, include, url
from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^test/$', views.testDateField, name='testDateField'),
)

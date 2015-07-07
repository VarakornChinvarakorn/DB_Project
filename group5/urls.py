from django.conf.urls import patterns, include, url
from group5 import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/status/$', views.table_user.as_view() , name = 'status'  ),
    #url(r'^/status/$', views.exampleCurrentUser , name = 'status'  ),
    url(r'^/status/$', views.table_status , name = 'status'  ),
    url(r'^/company/$', views.table_company , name = 'company'  ),
    url(r'^/form1/$', views.tablef1_status , name = 'form1'  ),
    url(r'^/addpet/$', views.table_addpet , name = 'addpet'  ),
    #url(r'^/(?P<pk>\d+)/statusof/$', views.statusof.as_view(), name='statusof'),
    #url(r'^/company/$', views.company , name = 'company'  ),
    #url(r'^/currentuser/$', views.exampleCurrentUser , name = 'currentuser'  ),
)

from django.conf.urls import patterns, include, url
from group7 import views
from django.contrib import admin
urlpatterns = patterns('',
#ex: /group7Project_Docs/
        url(r'^admin/', include(admin.site.urls)),
	url(r'^Project_Docs/$', views.home, name='index'),
        url(r'^/(?P<pk>\d+)/$', views.order.as_view(), name='order'),#order ok
        url(r'^Addorder/$', views.home, name='project_docs_add'),
#-----------------------------------------------------------------------------------------# file menu from Kon --not complete

#ex: /group7/Project_id/addorder/ --> EX: localhost:8000/group7/1/addorder/
	url(r'^/(?P<pk>\d+)/addorder/$', views.addorder.as_view(), name='addorder'),
	url(r'^/(?P<pk>\d+)/addorderview/$', views.addorderview, name='addorderview'),
#-----------------------------------------------------------------------------------------# Add Order
#ex: /group7/Project_id/orderinfo/ --> EX: localhost:8000/group7/1/orderinfo/

        url(r'^/(?P<pk>\d+)/orderinfoview/$', views.vieworderprint, name='orderprint'),
	url(r'^/(?P<pk>\d+)/orderinfo/$', views.orderinfo, name='orderinfo'),
#-----------------------------------------------------------------------------------------# Show OrderInfo
#ex: /group7/Project_id/addorderinfo/ --> EX: localhost:8000/group7/1/addorderinfo/
	url(r'^/(?P<pk>\d+)/addorderinfo/$', views.addorderinfo.as_view(), name='addorderinfo'),
	url(r'^/(?P<pk>\d+)/addorderinfoview/$', views.addorderinfoview, name='addorderinfoview'),
#-----------------------------------------------------------------------------------------# Add OrderInfo
#ex: /group7/Project_id/orderinfo/ --> EX: localhost:8000/group7/1/statusof/
	url(r'^/(?P<pk>\d+)/statusof/$', views.statusof.as_view(), name='statusof'),
        url(r'^/(?P<pk>\d+)/statusof/addstatusof/$', views.addstatusview.as_view(), name='addstatusof'),
        url(r'^/(?P<pk>\d+)/addstatusof/$', views.addstatus, name='addstatus'),
        url(r'^/(?P<info_id>\d+)/remove/$', views.removeOrder, name='removeOrder'),
        url(r'^/(?P<info_id>\d+)/orderinfo/remove/$', views.removeOrderinfo, name='removeOrderinfo'),
        url(r'^/(?P<pk>\d+)/orderinfo/edit/$', views.orderedit, name='eOrderinfo'),
        url(r'^/(?P<info_id>\d+)/editorf/$', views.editOrderinfo, name='editOrderinfo'),
        url(r'^/(?P<info_id>\d+)/statusof/remove/$', views.removeStatusof, name='removeStatusof'),
        url(r'^/(?P<pk>\d+)/statusof/requisition/$', views.viewrequi, name='requisition'),
        url(r'^/(?P<pk>\d+)/statusof/edit/$', views.statusofedit, name='eStatusof'),
        url(r'^/(?P<info_id>\d+)/editstf/$', views.editstatusof, name='editStatusof'),

)

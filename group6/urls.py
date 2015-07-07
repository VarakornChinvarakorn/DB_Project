from django.conf.urls import patterns, include, url
from group6 import views

urlpatterns = patterns('',
    url(r'^Project_Docs/$', views.index, name='project_docs_index'),
    url(r'^Project_Docs/create_3forms/$', views.create_3forms, name='project_docs_create_3forms'),
    url(r'^Project_Docs/create_3forms/add$', views.create_3forms_add, name='project_docs_create_3forms_add'),
    url(r'^Project_Docs/view_approveProject/(\d+)/$', views.approveProject, name='project_docs_approveProject'),
    url(r'^Project_Docs/view_offerProject/(\d+)/$', views.offerProject, name='project_docs_offerProject'),
    url(r'^Project_Docs/view_researchProject/(\d+)/$', views.researchProject, name='project_docs_researchProject'),
    url(r'^Project_Docs/view_timeLineProject/(\d+)/$', views.timeLineProject, name='project_docs_timeLineProject'),
    url(r'^Project_Docs/view_approveProject/(\d+)/print/$', views.approveProjectPrint, name='project_docs_approveProject_print'),
    url(r'^Project_Docs/view_offerProject/(\d+)/print/$', views.offerProjectPrint, name='project_docs_offerProject_print'),
    url(r'^Project_Docs/view_researchProject/(\d+)/print/$', views.researchProjectPrint, name='project_docs_researchProject_print'),
    url(r'^Project_Docs/view_timeLineProject/(\d+)/print/$', views.timeLineProjectPrint, name='project_docs_timeLineProject_print'),
    url(r'^Project_Docs/delete/(\d+)/$', views.deleteForm, name='project_docs_delete'),
    url(r'^Project_Docs/edit/(\d+)/$', views.edit_3forms, name='project_docs_edit'),
    url(r'^Project_Docs/edit/(\d+)/update$', views.edit_3forms_update, name='project_docs_edit_update'),
    #url(r'^testpdf/(\d+)/$', views.genpdf, name='genpdf'),
)

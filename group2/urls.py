from django.conf.urls import patterns, include, url
from group2 import views

urlpatterns = patterns('',
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dataStudent/$', views.data_student, name='data_student'),
    url(r'^dataStudentEdit/$', views.data_student_edit, name='data_student_edit'),
    url(r'^getdataStudentEdit/$', views.get_data_student_edit, name='get_data_student_edit'),
	url(r'^search_student/$', views.search_student, name='search_student'),
    url(r'^viyanipon/$', views.viyanipon, name='viyanipon'),
    url(r'^registeration/$', views.registeration, name='registeration'),
    url(r'^regisResult/$', views.regis_result, name='regis_result'),
    url(r'^schoolRecord/$', views.school_record, name='school_record'),
    url(r'^regis_result_nobutton/$', views.regis_result_nobutton, name='regis_result_nobutton'),
)

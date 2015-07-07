#--coding: utf-8--
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group2.models import *
from login.models import *
from datetime import datetime


def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user = user)
        return userprofile.type
    except:
        return 'admin'

def profile(request):
    template = 'group2/profile.html'    # get template
	
    if getUserType(request) != '0':
        template = 'group2/search_student.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj}

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
		
def data_student(request):
    template = 'group2/data_student.html'    # get template
	
    if getUserType(request) != '0':
        template = 'group2/data_student.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def data_student_edit(request):
    template = 'group2/data_student_edit.html'    # get template
	
    if getUserType(request) != '0':
        template = 'group2/data_student_edit.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def get_data_student_edit(request):
    template = 'group2/data_student.html'    # get template
	
    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        

    except: # can't get a Student object
        context = {}

    if 'term' in request.POST and request.POST['term']:
		term = request.POST['term']
		
		
    
    #DS = detailStudy(term=term)
    #DS.save()
		
    return render(
        request,
        template,
        context
    )
	
def search_student(request):
    template = 'group2/profile.html'    # get template
	
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        

    except: # can't get a Student object
        context = {}

    if 'search' in request.POST and request.POST['search']:
		search = request.POST['search']
		print search
		
		
    
    #DS = detailStudy(term=term)
    #DS.save()
		
    return render(
        request,
        template,
        context
    )
	
def registeration(request):
    template = 'group2/registeration.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )
		#Course = Course.objects.get(Course_ID = )
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )

def regis_result(request):
    template = 'group2/regis_result.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/regis_result.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def school_record(request):
    template = 'group2/school_record.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        number_table=Grade.objects.get(std_id = studentObj)
        course = Course.objects.get(Course_ID = number_table.Course_ID.Course_ID)
        #if len(number_table)==0 :
			#template = 'group2/error.html'
        #context = {'studentObj':studentObj,'number_table':number_table,'course':course}
        context['studentObj'] = studentObj
        context['number_table'] = number_table
        context['course'] = course
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}


    return render(
        request,
        template,
        context
    )
	
def viyanipon(request):
    template = 'group2/viyanipon.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/viyanipon.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )  


def regis_result_nobutton(request):
    template = 'group2/regis_result_nobutton.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    ) 
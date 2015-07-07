from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from group5.models import *
from django.views import generic
import django.shortcuts
from login.models import UserProfile,Student
from django.template import RequestContext
from group5.models import StatusPetition,studentG5,Internship
from django.db.models import Max


def table_status(request):
    thisuser = request.user
    currentUser = UserProfile.objects.get(user = thisuser)
    stu=Student.objects.get(userprofile_id=currentUser.id)
    stuG5= studentG5.objects.all()
    #pet= StatusPetition.objects.all()
    pet = StatusPetition.objects.filter(studentG5_id = stuG5)
    context = {'currentUser': currentUser,'stu':stu,'stuG5':stuG5,'pet':pet}
    return render(request, 'group5/status.html', context)

def table_company(request):
    com = Internship.objects.all()
    context = {'com': com}
    return render(request, 'group5/company.html', context)
    
def tablef1_status(request):
    state= StatusPetition.objects.all()
    stu=Student.objects.all()
    Pro= UserProfile.objects.all()
    context = {'state': state,'stu': stu,'Pro': Pro}
    return render(request, 'group5/form1department.html', context)
    
def table_addpet(request):
    stu_id = request.GET.get('id_student','')
    sex = request.GET.get('sex','')
    stu_year = request.GET.get('stu_year','')

    
    office = request.GET.get('office','')
    address = request.GET.get('address','')
    tel = request.GET.get('tel','')
    fax = request.GET.get('fax','')
    
    date1 = request.GET.get('date1','')
    month1 = request.GET.get('month1','')
    year1 = request.GET.get('year1','')
    date2 = request.GET.get('date2','')
    month2 = request.GET.get('month2','')
    year2 = request.GET.get('year2','')
    send = request.GET.get('send','')
    
    bf = str(year1)+"-"+str(month1)+"-"+str(date1)
    at = str(year2)+"-"+str(month2)+"-"+str(date2)
    
    
    thisuser = request.user
    currentUser = UserProfile.objects.get(user = thisuser)
    stu=Student.objects.get(userprofile_id=currentUser.id)
    stuG5= studentG5.objects.all()
    stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))
    stat2 = StatusPetition.objects.all()
    j = stat.values()
    j = j[0]
    if j == None:
        j = 0;
    
    if stu_year != '' :
        p=studentG5(studentID=stu_id,studentYear=stu_year,sex=sex)
        p.save()
        
        q=Internship(name_Internship=office.upper(),add_Internship=address,Tel=tel,Fax=fax)
        q.save()
    
        a = 0
        office = office.upper()
        for i in stat2 :
            if office == i.Internship_id :
                a = 1
        if a == 0:
            r=StatusPetition(NoPetition = j+1,StatusPetition='open',Date=bf,Date2=at,Internship_id=office,studentG5_id=stu_id,send = send)
            r.save()

    context = {'currentUser': currentUser,'stu':stu,'stuG5':stuG5,'stat':stat}
    return render(request, 'group5/form1new.html', context)
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group6.models import *
from group7.models import *
from login.models import *
from datetime import datetime
from django.views import generic
import datetime


def home(request):
	stu = ProjectG6.objects.all()
        teacher=[]
        for name in stu:
            teacher.append(Teacher.objects.get(id=name.teacher_id))
            
        return render(request, 'group7/home.html', {'object': stu,'teacher':teacher})
                
class order(generic.DetailView):
	model=ProjectG6
   	template_name='group7/order.html'
class addorder(generic.DetailView):
	model=ProjectG6
        template_name='group7/addorder.html'


        
def addorderview(request, pk):
	date=request.POST['date_order']
        name=request.POST['name']
        p=Order(Projectg7_id=pk,Date=date,name=name)   	
	p.save()
        url="/group7/"+pk
        return HttpResponseRedirect(url)
#----------------------------- Orderinfo -------------------------------------------#
def orderinfo(request,pk):
        s = Order.objects.get(id=pk)
        info=s.orderinfo_set.all()
        sum=0
        for price in info:
            sum+=price.Cost_total
        return render(request, 'group7/orderinfo.html', {'object': info,'sum':sum,'s':s})

#----------------------------- Add OrderInfo -------------------------------------------#
class addorderinfo(generic.DetailView):
	model=Order
        template_name='group7/addorderinfo.html'

def addorderinfoview(request, pk):
	itemname=request.POST['itemname_orderinfo']
	amount=request.POST['amount_orderinfo']
	price=request.POST['price_orderinfo']
        company=request.POST['company']
        id=request.POST['id']
        sum=int(price)*int(amount)
        p=Orderinfo(Order_id=pk,Item_name=itemname, Amount=amount,Company=company,OrderID=id, Cost=price, Cost_total=sum)   	
	p.save()
        url="/group7/"+pk+"/orderinfo/"
        return HttpResponseRedirect(url)
#----------------------------- StatusOf -------------------------------------------#
class statusof(generic.DetailView):
	model=Order
   	template_name= 'group7/statusof.html'
# Create your views here.
class addstatusview(generic.DetailView):
        model=Order
   	template_name= 'group7/addstatusof.html'
def addstatus(request,pk):
    date=request.GET.get('date_status')
    state = request.GET.get('state_status')
    more=request.GET.get('more')
    status=""
    if (request.GET.get('state_status')=="complete"):
        status="สมบูรณ์"
        state="ใบเบิกวัสดุ"
    else:
        status="ไม่สมบูรณ์"
    p=Status_Of(Order_id=pk,Date=date,State=state, Status=status ,Moreabout=more,Prove="Ok") 
    p.save()
    url="/group7/"+pk+"/statusof/"
    return HttpResponseRedirect(url)
    
def removeOrder(request,info_id): #Page Order for delete Order
	p=Order.objects.get(id=info_id)
        q=p.Projectg7_id
	p.delete()
	p.save
	url="/group7/"+str(q)
	return HttpResponseRedirect(url)
def removeOrderinfo(request,info_id): #Page Orderinfo for delete Orderinfo
	p=Orderinfo.objects.get(id=info_id)
        q=p.Order_id
	p.delete()
	p.save
	url="/group7/"+str(q)+"/orderinfo/"
	return HttpResponseRedirect(url)
        
def orderedit(request,pk):
        stu=Orderinfo.objects.get(id=pk)
            
        return render(request, 'group7/editorderinfo.html', {'object': stu})
    
    
def editOrderinfo(request,info_id): #Page Orderinfo for delete Orderinfo
        itemname=request.GET.get('itemname_orderinfo')
	amount=request.GET.get('amount_orderinfo')
	price=request.GET.get('price_orderinfo')
        company=request.GET.get('company')
        id=request.GET.get('id')
        sum=int(price)*int(amount)
        q=Orderinfo.objects.get(id=info_id)
	p=Orderinfo(id=info_id,Order_id=q.Order_id,Item_name=itemname, Amount=amount,Company=company,OrderID=id, Cost=price, Cost_total=sum)   	
	p.save()
	url="/group7/"+str(q.Order_id)+"/orderinfo/"
	return HttpResponseRedirect(url)
def removeStatusof(request,info_id): #Page Orderinfo for delete Orderinfo
	p=Status_Of.objects.get(id=info_id)
        q=p.Order_id
	p.delete()
	p.save
	url="/group7/"+str(q)+"/statusof/"
	return HttpResponseRedirect(url)
#----------------------------- View orderinfo -------------------------------------------#
class vieworderinfo(generic.DetailView):
	model=Order
   	template_name= 'group7/orderinfoview.html'
#----------------------------- View requisition -------------------------------------------#
def viewrequi(request,pk):
        now = datetime.datetime.now()
        project=ProjectG6.objects.get(id=pk)
	order = Order.objects.get(Projectg7_id=pk)
 
        return render(request, 'group7/requisitionview.html', {'order': order,'project':project,'date':now})

def vieworderprint(request,pk):
        now = datetime.datetime.now()
        
	order = Order.objects.get(id=pk)
        project=ProjectG6.objects.get(id=order.Projectg7_id)
        stu = ProjectG6.objects.all()
        teacher=[]
        for name in stu:
                teacher.append(Teacher.objects.get(id=name.teacher_id))
       
        return render(request, 'group7/orderinfoview.html', {'order': order,'teacher':teacher,'project':project,'date':now})
        
def statusofedit(request,pk):
        stu=Status_Of.objects.get(id=pk)
        return render(request, 'group7/editstatusof.html', {'object': stu})
        
def editstatusof(request,info_id): #Page Orderinfo for delete Orderinfo
	date=request.GET.get('date_status')
    	state = request.GET.get('state_status')
    	more=request.GET.get('more')
    	status=""
    	if (request.GET.get('state_status')=="complete"):
        	status="สมบูรณ์"
        	state="ใบเบิกวัสดุ"
    	else:
        	status="ไม่สมบูรณ์"
	q=Status_Of.objects.get(id=info_id)
    	p=Status_Of(id=info_id,Order_id=q.Order_id,Date=date,State=state, Status=status ,Moreabout=more,Prove="Ok") 
    	p.save()
    	url="/group7/"+str(q.Order_id)+"/statusof/"
    	return HttpResponseRedirect(url)
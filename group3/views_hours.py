#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from login.models import *
from group3.models import *

def add_work(request, employeeID):
    template = 'group3/worker/add_work.html'
    context = {}
    employee = HourlyEmployee.objects.get(id=employeeID)
    context["employee"] = employee

    if request.method == "POST":
        startTime_hour   = request.POST["startTime_hour"]
        startTime_minute = request.POST["startTime_minute"]
        endTime_hour     = request.POST["endTime_hour"]
        endTime_minute   = request.POST["endTime_minute"]

        startTime = str(startTime_hour + ":" + startTime_minute + ":00")
        endTime   = str(endTime_hour   + ":" + endTime_minute   + ":00")

        workObj = Work(
            startTime = startTime,
            endTime   = endTime,
            employee  = employee
        )
        workObj.save()
        return HttpResponseRedirect(reverse('group3:returnsearch', args=[employeeID]))


    return render(
        request,
        template,
        context
    )

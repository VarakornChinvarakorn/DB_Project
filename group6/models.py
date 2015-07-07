from django.db import models
from login.models import *

class ProjectG6(models.Model):
    student = models.ManyToManyField(Student) #link to Student many to many
    teacher = models.ForeignKey(Teacher) #link to Teacher entity one to one
    name_thai = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    yearOfEducation = models.IntegerField(default = 1)
    objective = models.TextField()
    reason = models.TextField()
    scope = models.TextField()
    benefit = models.TextField()

class ResearchProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    numberOfPeople = models.IntegerField(default = 1)

class OfferProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    priceOfMaterial = models.FloatField(default=0.00)
    priceOfOther = models.FloatField(default=0.00)

class ApproveProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    student = models.ForeignKey(Student) #link to Student one to one
    course = models.CharField(max_length=200)
    semesterEnd = models.CharField(max_length=200)
    yearEnd = models.CharField(max_length=200)
    credit = models.IntegerField(default = 3)

class TimeLineForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    day = models.IntegerField(default = 1)
    month = models.CharField(max_length=200)
    year= models.IntegerField(default = 1)
    note = models.TextField()

class StepInTimeLine(models.Model):
    timeline = models.ForeignKey(TimeLineForm) #Link to TimeLineForm entity Many to one
    numberOfProcess = models.IntegerField(default = 1)
    processDescription = models.CharField(max_length=200)
    month1 = models.BooleanField(default=False)
    month2 = models.BooleanField(default=False)
    month3 = models.BooleanField(default=False)
    month4 = models.BooleanField(default=False)
    month5 = models.BooleanField(default=False)
    month6 = models.BooleanField(default=False)
    month7 = models.BooleanField(default=False)
    month8 = models.BooleanField(default=False)
    month9 = models.BooleanField(default=False)
    month10 = models.BooleanField(default=False)
    month11 = models.BooleanField(default=False)
    month12 = models.BooleanField(default=False)
    

#-*- coding: utf-8 -*-
from django.db import models
from login.models import *


class Department(models.Model):
    #code
    Department_ID = models.IntegerField(primary_key=True, max_length=10)
    Department_Name = models.CharField( max_length=100 )

class Course(models.Model):
    #code
    Course_ID = models.IntegerField(primary_key=True, max_length=10)
    Course_Name = models.CharField( max_length=100 )
    Department_ID = models.ForeignKey(Department)
    Credit = models.CharField( max_length=10 )
    Describe = models.CharField( max_length=1000, blank=True )
    Course_Before = models.IntegerField( max_length=10, blank=True )
	
class Section(models.Model):
    Section = models.IntegerField(primary_key=True, max_length=7)
    Course_ID = models.ForeignKey(Course)
    classroom = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()
    Teacher_ID = models.ForeignKey(Teacher)
    
    dateChoices = (
    ('M', 'Monday'),
    ('T', 'Tuesday'),
    ('W', 'Wednesday'),
    ('H', 'Thursday'),
    ('F', 'Friday'),
    ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)
	
class Grade(models.Model):
    #code
    std_id = models.ForeignKey(Student)
    Course_ID = models.ForeignKey(Course)
    year        = models.IntegerField(max_length=10)
    term        = models.IntegerField(max_length=1)
    gradeChoices = (
    ('0', 'F'),
    ('1', 'D'),
    ('2', 'D+'),
    ('3', 'C'),
    ('4', 'C+'),
    ('5', 'B'),
    ('6', 'B+'),
    ('7', 'A'),
	('8', 'FA'),
	('9', 'I'),
    )
    Grade = models.CharField( max_length=1, choices=gradeChoices )
    Section = models.ForeignKey(Section)
    def __unicode__(self):
        return "Year "+str(self.year)+"  Term "+  str(self.term)



class Teacher_Course(models.Model):
    #code
    shortname = models.ForeignKey(Teacher)
    Course_ID = models.ForeignKey(Course)
    Section = models.ForeignKey(Section)

	
class scheme(models.Model):
    Course_ID = models.ForeignKey(Course)
    schemeChoices = (
    ('0', 'หลักสูตรปรับปรุง Cpr.E 54'),
    ('1', 'หลักสูตรปรับปรุง EE 51'),
    ('2', 'หลักสูตรปรับปรุง ECE 55')
    )
    scheme = models.CharField(max_length=1, choices=schemeChoices)
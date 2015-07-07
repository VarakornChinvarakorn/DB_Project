#-*- coding: utf-8 -*-
from django.db import models
from login.models import *
import datetime, time
# Create your models here.
class Prof2Lang(models.Model):
    # the professor ID is primary key
    profID = models.CharField(primary_key=True, max_length=10)                      # 1. * profID
    # professor profile
    firstName = models.CharField(max_length=50)                                     # 2. * firstName
    lastName = models.CharField(max_length=80)                                      # 3. * lastName
    shortName = models.CharField(max_length=3)                                      # 4. * shortName

    tell = models.CharField(blank=True, max_length=15)                              # 5. tell
    email = models.EmailField(blank=True)                                           # 6. email
    sahakornAccount = models.CharField(blank=True, max_length=100, default=True)    # 7. sahakornAccount

    department = models.CharField(max_length=200, blank=True, default="")           # 8. department
    faculty = models.CharField(max_length=200, blank=True, default="")              # 9. faculty

    typeChoices = (
        ('0','อาจารย์ในภาควิชา'),
        ('1','อาจารย์นอกภาควิชา'),
        ('2','อาจารย์พิเศษ')
    )
    type = models.CharField(max_length=1, choices=typeChoices)                      # 10. * type ประเภทอาจารย์

    prefix_name_choices = (
        ('0', 'นาย'),       # Mr.
        ('1', 'นาง'),       # Mrs.
        ('2', 'นางสาว'),    # Miss.
        ('3', 'ดร.')        # Dr.
    )
    prefix_name  = models.CharField(max_length=1, choices=prefix_name_choices)      # 11. * คำนำหน้าชื่อ

    academic_position_choice = (
        ('0', ''),
        ('1', 'ผู้ช่วยศาสตราจารย์'),    # ตัวย่อไทย ผศ.  ตัวย่อแบบอเมริกา  Asst.Prof.   มาจาก Assistant Professor
        ('2', 'รองศาสตราจารย์'),     # ตัวย่อไทย รศ.  ตัวย่อแบบอเมริกา  Assoc.Prof.  มาจาก Associate Professor
        ('3', 'ศาสตราจารย์')          # ตัวย่อไทย ศ.   ตัวย่อแบบอเมริกา Prof.         มาจาก Professor
    )
    academic_position = models.CharField(max_length=1, choices=academic_position_choice)    # 12. ตำแหน่งทางวิชาการ

    def __unicode__(self):
        return self.firstName + " " + self.lastName

class Subject(models.Model):
    subjectID = models.CharField(primary_key=True, max_length=9)
    subjectName = models.CharField(max_length=200)

    def __unicode__(self):
        return self.subjectName

class Section(models.Model):
    section = models.CharField(max_length=7)
    subject = models.ForeignKey(Subject)
    classroom = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()

    dateChoices = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)

    def __unicode__(self):
        return self.section + " " + self.subject.subjectName

    class meta:
        unique_together = ('section', 'subject')

class Teach(models.Model):
    prof = models.ForeignKey(Prof2Lang, blank=True, null=True)
    subject = models.ForeignKey(Subject)
    section = models.ForeignKey(Section)

class HourlyEmployee(models.Model):
    user = models.OneToOneField(UserProfile)
    numberTaxpayment = models.CharField(max_length=20, blank=True, default="")  # เลขประจำตัวผู้เสียภาษี
    status = models.CharField(max_length=50, blank=True, default="")            # ตำแหน่ง
    employmentRate = models.FloatField(max_length=10, default=0.0)              # อัตรารายได้

    def __unicode__(self):
        return self.user.firstname_en + " " + self.user.lastname_en

class Work(models.Model):
    releaseDate = models.DateField(auto_now=True)   # วันที่เพิ่มข้อมูล
    startTime = models.TimeField()                      # เวลาเริ่มทำงาน
    endTime = models.TimeField()                        # เวลาเลิกงาน
    note = models.TextField(blank=True)                 # หมายเหตุ
    employee = models.ForeignKey(HourlyEmployee)        # เป็นของพนักงานคนใด
    day = models.DateTimeField(auto_now=True)
    class meta:
        unique_together = ('employee', 'id')
        
    def get_time_diff(self):
        if str(self.endTime) == '00:00:01':
            return ''
        else:
            t_start = str(self.startTime.hour)+':'+str(self.startTime.minute) # time that employee come to work.
            t_end = str(self.endTime.hour)+':'+str(self.endTime.minute) # time that employee go home
            diff_min = int(t_end.split(':')[1]) - int(t_start.split(':')[1])    # calculate differ value of come_time
            diff_hour = int(t_end.split(':')[0]) - int(t_start.split(':')[0])  # calculate differ value of back_time
            if diff_min < 0:
                diff_min = 60 - diff_min
            return str(diff_hour) + ':'+str(diff_min)
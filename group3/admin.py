#-*- coding: utf-8 -*-
from django.contrib import admin
from group3.models import *

# Register your models here.
class Prof2LangAdmin(admin.ModelAdmin):
    list_display = ('profID', 'academic_position', 'prefix_name', 'firstName', 'lastName', 'shortName', 'department', 'faculty', 'type')

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subjectID', 'subjectName')
    fieldsets = [
        ('Subject ID',      {'fields': ['subjectID']}),
        ('Subject Name',    {'fields': ['subjectName']}),
    ]
    inlines = [SectionInline]

class SectionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'section', 'date', 'startTime', 'endTime', 'classroom')

class TeachAdmin(admin.ModelAdmin):
    list_display = ('prof', 'subject', 'section')

class WorkInline(admin.StackedInline):
    model = Work
    extra = 1

class HourlyEmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'numberTaxpayment', 'status', 'employmentRate')
    inlines = [WorkInline]

class WorkAdmin(admin.ModelAdmin):
    list_display = ('employee', 'releaseDate', 'startTime', 'endTime', 'note')

admin.site.register(Prof2Lang, Prof2LangAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Teach, TeachAdmin)

admin.site.register(HourlyEmployee, HourlyEmployeeAdmin)
admin.site.register(Work, WorkAdmin)
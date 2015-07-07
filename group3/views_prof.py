#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from login.models import *
from group3.models import *
from group3.views import genProfID, prof_add_in

def prof_index(request):
    prof_add_in()   # add Teacher to Prof2Lang
    template = 'group3/prof/prof_index.html'
    context = {}

    profList = Prof2Lang.objects.all().order_by('profID')
    context['profList'] = profList
    return render(
        request,
        template,
        context
    )

def prof_add(request, context={}):
    template = 'group3/prof/prof_form.html'
    #context = {}

    context['menuName'] = 'เพิ่มข้อมูลอาจารย์ผู้สอน'
    context['prof_in_formAction'] = '0'
    context['prof_out_formAction'] = '0'
    context['prof_special_formAction'] = '0'
    context['teachers'] = Teacher.objects.all().order_by('shortname')

    return render(
        request,
        template,
        context
    )

def prof_add_out(request):
    error = False
    errorMessage = []
    context = {}

    context['prof_out'] = 'active'

    if request.method == 'POST':
        profID              = genProfID()                       # 1. profID
        firstName           = request.POST['firstName']         # 2. firstName
        lastName            = request.POST['lastName']          # 3. lastName
        shortName           = request.POST['shortName']         # 4. shortName
        tell                = request.POST['tell']              # 5. tell
        email               = request.POST['email']             # 6. email
        sahakornAccount     = request.POST['sahakornAccount']   # 7. sahakornAccount
        department          = request.POST['department']        # 8. department
        faculty             = request.POST['faculty']           # 9. faculty
        type                = '1'                               # 10. type 1 is อาจารย์นอกภาควิชา
        prefix_name         = request.POST['prefix_name']       # 11. prefix_name
        academic_position   = request.POST['academic_position'] # 12. academic_position

        # ปรับ shortName ให้เป็นตัวพิมพ์ใหญ่
        shortName = str(shortName).upper()

        # ตรวจสอบดูว่า profID ซ้ำหรือไม่
        try:
            test = Prof2Lang.objects.get(profID = profID)
            error = True
            errorMessage.append('รหัสอาจารย์นี้มีในฐานข้อมูลแล้ว')
        except:
            pass

        if error:
            context['profID']           = profID            # 1. profID
            context['firstName']        = firstName         # 2. firstName
            context['lastName']         = lastName          # 3. lastName
            context['shortName']        = shortName         # 4. shortName
            context['tell']             = tell              # 5. tell
            context['email']            = email             # 6. email
            context['sahakornAccount']  = sahakornAccount   # 7. sahakornAccount
            context['department']       = department        # 8. department
            context['faculty']          = faculty           # 9. faculty

            context['prof_out_errorMessage']     = errorMessage
        else:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID          = profID,           # 1. profID
                firstName       = firstName,        # 2. firstName
                lastName        = lastName,         # 3. lastName
                shortName       = shortName,        # 4. shortName
                tell            = tell,             # 5. tell
                email           = email,            # 6. email
                sahakornAccount = sahakornAccount,  # 7. sahakornAccount
                department      = department,       # 8. department
                faculty         = faculty,          # 9. faculty
                type            = type,             # 10. type
                prefix_name     = prefix_name,      # 11. prefix_name
                academic_position = academic_position # 12. academic_position
            )

            # save new Prof2Lang object into database
            newProf.save()
            context['prof_out_successMessage'] = "เพิ่มข้อมูลอาจารย์ผู้สอนนอกภาควิชาเรียบร้อยแล้ว"
    return prof_add(request, context)

def prof_add_special(request):
    error = False
    errorMessage = []
    context = {}

    context['prof_special'] = 'active'

    if request.method == 'POST':
        profID              = genProfID()                       # 1. profID
        firstName           = request.POST['firstName']         # 2. firstName
        lastName            = request.POST['lastName']          # 3. lastName
        shortName           = request.POST['shortName']         # 4. shortName
        tell                = request.POST['tell']              # 5. tell
        email               = request.POST['email']             # 6. email
        sahakornAccount     = request.POST['sahakornAccount']   # 7. sahakornAccount
        department          = ''                                # 8. department is empty
        faculty             = ''                                # 9. faculty is empty
        type                = '2'                               # 10. type 1 is อาจารย์พิเศษ
        prefix_name         = request.POST['prefix_name']       # 11. prefix_name
        academic_position   = request.POST['academic_position'] # 12. academic_position

        # ปรับ shortName ให้เป็นตัวพิมพ์ใหญ่
        shortName = str(shortName).upper()

        # ตรวจสอบดูว่า profID ซ้ำหรือไม่
        try:
            test = Prof2Lang.objects.get(profID = profID)
            error = True
            errorMessage.append('รหัสอาจารย์นี้มีในฐานข้อมูลแล้ว')
        except:
            pass

        if error:
            context['profID']           = profID            # 1. profID
            context['firstName']        = firstName         # 2. firstName
            context['lastName']         = lastName          # 3. lastName
            context['shortName']        = shortName         # 4. shortName
            context['tell']             = tell              # 5. tell
            context['email']            = email             # 6. email
            context['sahakornAccount']  = sahakornAccount   # 7. sahakornAccount

            context['prof_special_errorMessage']     = errorMessage
        else:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID          = profID,           # 1. profID
                firstName       = firstName,        # 2. firstName
                lastName        = lastName,         # 3. lastName
                shortName       = shortName,        # 4. shortName
                tell            = tell,             # 5. tell
                email           = email,            # 6. email
                sahakornAccount = sahakornAccount,  # 7. sahakornAccount
                department      = department,       # 8. department
                faculty         = faculty,          # 9. faculty
                type            = type,             # 10. type
                prefix_name     = prefix_name,      # 11. prefix_name
                academic_position = academic_position # 12. academic_position
            )

            # save new Prof2Lang object into database
            newProf.save()
            context['prof_special_successMessage'] = "เพิ่มข้อมูลอาจารย์พิเศษเรียบร้อยแล้ว"
    return prof_add(request, context)

def prof_view(request, profID):
    template = 'group3/prof/prof_view.html'
    context = {}
    try:
        prof = Prof2Lang.objects.get(profID = profID)
        context['prof'] = prof
    except:
        pass
    return render(
        request,
        template,
        context
    )

def prof_update(request, profID):
    template = 'group3/prof/prof_form.html'
    context = {}

    # get Prof2Lang object
    prof = Prof2Lang.objects.get(profID = profID)

    context['prof']         = prof              # Prof2Lang object
    context['menuName']     = 'แก้ไขข้อมูล'      # name of menu in breadcrumb
    context['prof_out_formAction']   = '1'               # select action of form
    context['update']       = True

    error = False
    errorMessage = []

    context['profID']           = prof.profID           # 1. profID
    context['firstName']        = prof.firstName        # 2. firstName
    context['lastName']         = prof.lastName         # 3. lastName
    context['shortName']        = prof.shortName        # 4. shortName
    context['tell']             = prof.tell             # 5. tell
    context['email']            = prof.email            # 6. email
    context['sahakornAccount']  = prof.sahakornAccount  # 7. sahakornAccount
    context['department']       = prof.department       # 8. department
    context['faculty']          = prof.faculty          # 9. faculty

    if request.method == 'POST':
        firstName       = request.POST['firstName']         # 2. firstName
        lastName        = request.POST['lastName']          # 3. lastName
        shortName       = request.POST['shortName']         # 4. shortName
        tell            = request.POST['tell']              # 5. tell
        email           = request.POST['email']             # 6. email
        sahakornAccount = request.POST['sahakornAccount']   # 7. sahakornAccount
        department      = request.POST['department']        # 8. department
        faculty         = request.POST['faculty']           # 9. faculty

        # ปรับ shortName ให้เป็นตัวพิมพ์ใหญ่
        shortName = str(shortName).upper()

        if error:
            context['firstName']        = firstName         # 2. firstName
            context['lastName']         = lastName          # 3. lastName
            context['shortName']        = shortName         # 4. shortName
            context['tell']             = tell              # 5. tell
            context['email']            = email             # 6. email
            context['sahakornAccount']  = sahakornAccount   # 7. sahakornAccount
            context['department']       = department        # 8. department
            context['faculty']          = faculty           # 9. faculty

            context['prof_out_errorMessage']     = errorMessage
        else:
            prof.firstName          = firstName
            prof.lastName           = lastName
            prof.shortName          = shortName
            prof.tell               = tell
            prof.email              = email
            prof.sahakornAccount    = sahakornAccount
            prof.department         = department
            prof.faculty            = faculty
            prof.save()
            return HttpResponseRedirect(reverse('group3:prof_view', args=[prof.profID]))

    return render(
        request,
        template,
        context
    )

def prof_delete(request, profID):
    try:
        prof = Prof2Lang.objects.get(profID = profID)   # get Prof2Lang object
        teachList = prof.teach_set.all()                # get all Teach of this Prof2Lang object
        # set all Teach of this Prof2Lang as None
        for teach in teachList:
            teach.prof = None
            teach.save()
        # delete this Prof2Lang object
        prof.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('group3:prof_index'))

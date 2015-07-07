#-*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from login.models import UserProfile
import django.shortcuts
import time, datetime
from group3.models import *
from django.http import HttpResponse
from fpdf import FPDF

from django.contrib.auth.models import User
# Create your views here.
def genProfID():
    profList = Prof2Lang.objects.all().order_by('profID')
    if len(profList) > 0:
        lastProf = profList[len(profList)-1]
        id = int(lastProf.profID) + 1
        return str(id)
    else:
        return '1'

def prof_add_in():
    teachers = Teacher.objects.all()
    if len(teachers) > 0:
        for teacher in teachers:
            profID      = genProfID()                       # 1. profID
            firstName   = teacher.userprofile.firstname_th  # 2. firstName
            lastName    = teacher.userprofile.lastname_th   # 3. lastName
            shortName   = str(teacher.shortname).upper()    # 4. shortName
            tell        = teacher.userprofile.tel           # 5. tell
            email       = teacher.userprofile.user.email    # 6. email
            sahakornAccount = ''                            # 7. sahakornAccount
            department  = 'วิศวกรรมไฟฟ้าและคอมพิวเตอร์'     # 8. department
            faculty     = 'วิศวกรรมศาสตร์'                  # 9. faculty
            type        = '0'                               # 10. type 0 is อาจารย์ในภาค
            prefix_name = teacher.userprofile.prefix_name   # 11. prefix_name
            academic_position = teacher.academic_position   # 12. academic_position

            # check prof is duplicate
            try:
                prof = Prof2Lang.objects.get(shortName = shortName)
                # update prof
                prof.firstName      = firstName         # 2. firstName
                prof.lastName       = lastName          # 3. lastName
                prof.shortName      = shortName         # 4. shortName
                prof.tell           = tell              # 5. tell
                prof.email          = email             # 6. email
                prof.sahakornAccount= sahakornAccount   # 7. sahakornAccount
                prof.department     = department        # 8. department
                prof.faculty        = faculty           # 9. faculty
                prof.type           = type              # 10 .type
                prof.prefix_name    = prefix_name       # 11. prefix_name
                prof.academic_position=academic_position# 12. academic_position
                prof.save()
            except:
                # add new prof
                newProf = Prof2Lang(
                    profID          = profID,           # 1. profID
                    firstName       = firstName,        # 2. firstName
                    lastName        = lastName,         # 3. lastName
                    shortName       = shortName,        # 4, shortName
                    tell            = tell,             # 5. tell
                    email           = email,            # 6. email
                    sahakornAccount = sahakornAccount,  # 7. sahakornAccount
                    department      = department,       # 8. department
                    faculty         = faculty,          # 9. faculty
                    type            = type,             # 10. type
                    prefix_name     = prefix_name,      # 11. prefix_name
                    academic_position=academic_position # 12. academic_position
                )
                newProf.save()

def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user = user)
        return userprofile.type
    except:
        return 'admin'

def prof2lang_index(request):
    prof_add_in()   # add Teacher to Prof2Lang
    template = 'group3/prof2lang_index.html'    # get template
    context = {}
    teachList = Teach.objects.all()     # get all Prof2Lang objects

    # get current user type
    # user type is Student that can not access this system
    if getUserType(request) == '0':
        template = 'group3/disable_student.html'
        return render(request, template, {})

    context['teachList'] = teachList
    return render(
        request,
        template,
        context
    )

def prof2lang_view(request, profID):
    prof_add_in()   # add Teacher to Prof2Lang
    template = 'group3/prof2lang_view.html'             # get view template

    # get current user type
    # user type is Student that can not access this system
    if getUserType(request) == '0':
        template = 'group3/disable_student.html'
        return render(request, template, {})

    try:
        teachObj = Teach.objects.get(pk = int(profID))  # get a Teach object
        context = {'teachObj': teachObj}

        # get all Prof2Lang objects
        profList = Prof2Lang.objects.all().order_by('shortName')
        context['profList'] = profList

        # get all Subject objects
        subjectList = Subject.objects.all().order_by('subjectID')
        context['subjectList'] = subjectList

        # get all Section objects
        sectionList = teachObj.subject.section_set.all().order_by('section')
        context['sectionList'] = sectionList

    except: # can't get a Teach object
        context = {}

    return render(
        request,
        template,
        context
    )

def prof2lang_add(request, option = '0'):
    prof_add_in()   # add Teacher to Prof2Lang
    template = 'group3/prof2lang_add.html'
    # get all Prof2Lang objects
    prof2langObj = Prof2Lang.objects.all().order_by('shortName')
    # get all Subject objects
    subjectObj = Subject.objects.all().order_by('subjectID')

    # get current user type
    # user type is Student that can not access this system
    if getUserType(request) == '0':
        template = 'group3/disable_student.html'
        return render(request, template, {})

    # option 0 is get prof2lang_add web page
    if request.method == 'GET' and option == '0':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
        }
    # option 1 is add Prof2Lang object success
    elif option == '1':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfSuccess': True,
        }
    # option 2 is add Prof2Lang object not success
    elif option == '2':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfError': True,
        }
    # option 3 is add Subject object success
    elif option == '3':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectSuccess': True
        }
    # option 4 is add Subject object not success
    elif option == '4':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectError': True
        }
    # option 5 is add Section object success
    elif option == '5':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionSuccess': True
        }
    # option 6 is add Section object not success
    elif option == '6':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionError': True
        }
    # option 7 is add Teach object
    elif option == '7':
        if request.method == 'POST':
            try:
                # get data from html template
                # get object of Prof2Lang
                profID = request.POST['selectProf']
                if profID == 'null':
                    prof = None
                else:
                    prof = Prof2Lang.objects.get(profID = profID)

                # get object of Subject
                subjectID = request.POST['selectSubject']
                subject = Subject.objects.get(subjectID = subjectID)

                # get object of Section
                sectionID = request.POST['selectSection']
                section = Section.objects.get(id = sectionID)

                newTeach = Teach(
                    prof = prof,
                    subject = subject,
                    section = section
                )
                newTeach.save()
                context = {
                    'prof2langObj': prof2langObj,
                    'subjectObj': subjectObj,
                    'addTeachSuccess': True
                }

            except:
                context = {
                    'prof2langObj': prof2langObj,
                    'subjectObj': subjectObj,
                    'addTeachError': True
                }
        else:
            context = {
                'prof2langObj': prof2langObj,
                'subjectObj': subjectObj,
                'addTeachError': True
            }
    # option 8 Section is duplicate
    elif option == '8':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'sectionDuplicate': True
        }
    else:
        return prof2lang_index(request)



    return render(
        request,
        template,
        context
    )

# This function for get data and create new Prof2Lang object.
def addProf(request):
    if request.method == 'POST':
        # get data from html template
        profID      = request.POST['profID']
        firstName   = request.POST['firstName']
        lastName    = request.POST['lastName']
        shortName   = request.POST['shortName']
        tell        = request.POST['tell']
        email       = request.POST['email']
        sahakornAccount = request.POST['sahakornAccount']
        department  = request.POST['department']
        faculty     = request.POST['faculty']

        # check profID is duplicate
        try:
            prof = Prof2Lang.objects.get(profID = profID)
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['2']))
        except:
            pass

        try:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID = profID,
                firstName = firstName,
                lastName = lastName,
                shortName = shortName,
                tell = tell,
                email = email,
                sahakornAccount = sahakornAccount,
                department = department,
                faculty = faculty
            )
            # save new Prof2Lang object into database
            newProf.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['1']))
        except Exception, e:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['2']))

# This function for get data and create new Subject object.
def addSubject(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            subjectID = request.POST['subjectID']
            subjectName = request.POST['subjectName']

            # create new Subject object
            newSubject = Subject(
                subjectID = subjectID,
                subjectName = subjectName
            )
            # save new Subject object into database
            newSubject.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['3']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['4']))

# This function for get data and create new Section object
def addSection(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            section = request.POST['section']
            subject = request.POST['subject']
            classroom = request.POST['classroom']
            startTime_hour = request.POST['startTime_hour']
            startTime_minute = request.POST['startTime_minute']
            endTime_hour = request.POST['endTime_hour']
            endTime_minute = request.POST['endTime_minute']
            date = request.POST['date']

            # create startTime
            startTime = startTime_hour + ":" + startTime_minute + ":" + "00"
            # create endTime
            endTime = endTime_hour + ":" + endTime_minute + ":" + "00"
            # get Subject object that selected
            subjectObj = Subject.objects.get(subjectID = subject)

            allSection = subjectObj.section_set.all()
            for sec in allSection:
                if str(sec.section).upper() == str(section).upper():
                    return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['8']))

            section = str(section).upper()
            # create new Section object
            newSection = Section(
                section = section,
                subject = subjectObj,
                classroom = classroom,
                startTime = startTime,
                endTime = endTime,
                date = date
            )
            # save new Section object into database
            newSection.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['5']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['6']))

def genpdf(request, profID): # use to generate pdf file for lend another teacher.
    teachObj = Teach.objects.get(pk= int(profID))   # get all objects teacher.
    pdf = FPDF('P', 'mm', 'A4')    # start pdf file
    pdf.add_page()                   # begin first page.
    
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)  # add font
    pdf.set_font('DejaVu', '', 14)              # set font and font size
    
    pdf.image('group3/trarachakarn.png',30,25,15)   # insert image
    pdf.ln(25)    # new line
    
    proID = ''
    firstname = ''
    lastname = ''
    shortname = ''
    department = ''
    faculty = ''
    sahakornAccount = ''
    tell = ''
    email = ''
    
    subjectID = ''
    subjectName = ''
    sec = ''
    time = ''
    day = ''
    
    try: # prefix_name and academic_name
        academicPosition = teachObj.prof.academic_position
        if (academicPosition == '0'):
            academicPosition = u''
            try:
                pre_name = teachObj.prof.prefix_name
                if (pre_name == '0') or (pre_name == '1') or (pre_name == '2'):
                    pre_name = u'อ. '
                else:
                    pre_name = u'ดร. '
            except:
                pre_name = u'อ. '
        elif academicPosition == '1':
            academicPosition = u'ผู้ช่วยศาสตราจารย์ '
            short_academicPosition = u'ผศ.'
            try:
                pre_name = teachObj.prof.prefix_name
                if pre_name == '3':
                    pre_name = u'ดร.'
                else:
                    pre_name = ''
            except:
                pre_name =''
        elif academicPosition == '2':
            academicPosition =  u'รองศาสตราจารย์ '
            short_academicPosition =  u'รศ.'
            try:
                pre_name = teachObj.prof.prefix_name
                if pre_name == '3':
                    pre_name = u'ดร.'
                else:
                    pre_name = ''
            except:
                pre_name =''
        else:
            academicPosition = u'ศาสตราจารย์ '
            short_academicPosition = u'ศ.'
            try:
                pre_name = teachObj.prof.prefix_name
                if pre_name == '3':
                    pre_name = u'ดร.'
                else:
                    pre_name = ''
            except:
                pre_name =''
    except:
        academicPosition = ''
    
    try: # check all data for beware blank data.
        proID = teachObj.prof.shortName
    except:
        proID = 'None'

    try:
        firstname = teachObj.prof.firstName
    except:
        firstname = 'None'
 
    try:
        lastname = teachObj.prof.lastName
    except:
        lastname = 'None'

    try:
        shortname  = teachObj.prof.shortName
    except:
        shortname = 'None'

    try:
        department = teachObj.prof.department
    except:
        department = 'None'
    
    try:
        faculty = teachObj.prof.faculty
    except:
        faculty = 'None'

    try:
        sahakornAccount = teachObj.prof.sahakornAccount
    except:
        sahakornAccount = 'None'

    try:
        tell = teachObj.prof.tell
    except:
        tell = 'None'

    try:
        email = teachObj.prof.email
    except:
        email = 'None'
    
    try:
        subjectID = teachObj.subject.subjectID
    except:
        subjectID = 'None'
        
    try:
        subjectName = teachObj.subject.subjectName
    except:
        subjectName = 'None'
        
    try:
        sec = teachObj.section.section
    except:
        sec = 'None'
    
    try:
        time = str(teachObj.section.startTime)
    except:
        time = 'None'
        
    try:
        day = teachObj.section.date
        if day == 'M':
            day = u'จันทร์'
        elif day == 'T':
            day = u'อังคาร'
        elif day == 'W':
            day = u'พุธ'
        elif day == 'H':
            day = u'พฤหัสบดี'
        elif day == 'F':
            day = u'ศุกร์'
        elif day == 'S':
            day = u'เสาร์'
        else:
            day = u'อาทิตย์'
    except:
        day = 'None'
        
    pdf.add_font('THSarabun Bold', '', 'THSarabun Bold.ttf', uni=True)  # thai font bold
    pdf.set_font('THSarabun Bold', '', 29)
    pdf.cell(72, 10, u'')
    pdf.cell(0, 10, u' บันทึกข้อความ')
    pdf.ln(10)
    pdf.add_font('THSarabun Bold', '', 'THSarabun Bold.ttf', uni=True)  # thai font
    pdf.set_font('THSarabun Bold', '', 20)
    pdf.cell(19, 10, u'')
    pdf.cell(22, 10, u'ส่วนราชการ')
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.set_font('THSarabun', '', 16)
    pdf.cell(0, 11, u'  ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ คณะวิศวกรรมศาสตร์  โทร. ๘๕๑๘')
    pdf.line(55,52.5,180,52.5)
    pdf.ln(8)
    pdf.add_font('THSarabun Bold', '', 'THSarabun Bold.ttf', uni=True)
    pdf.set_font('THSarabun Bold','', 20)
    pdf.cell(19, 10, u'')
    pdf.cell(5, 10, u'ที่')
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.set_font('THSarabun', '', 16)
    pdf.cell(70, 10, u'   วฟ')
    pdf.add_font('THSarabun Bold', '', 'THSarabun Bold.ttf', uni=True)
    pdf.set_font('THSarabun Bold','', 20)
    pdf.cell(0, 10, u'วันที่')
    pdf.line(34,60.5,180,60.5)
    pdf.ln(8)
    pdf.cell(19, 10, u'')
    pdf.cell(11, 10, u'เรื่อง')
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.set_font('THSarabun', '', 16)
    pdf.cell(0, 11, u'การจัดการเรียนการสอนสำหรับนักศึกษาโครงการพิเศษ(สองภาษา)')
    pdf.line(40,68.5,180,68.5)
    pdf.ln(8)
    pdf.add_font('THSarabun Bold', '', 'THSarabun Bold.ttf', uni=True)
    pdf.set_font('THSarabun Bold','', 20)
    pdf.cell(19, 10, u'')
    pdf.cell(10, 10, u'เรียน')
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.set_font('THSarabun', '', 16)
    pdf.cell(24, 11, u'หัวหน้าภาควิชา' + department)
    pdf.ln(8)
    pdf.cell(45, 10, u'')
    pdf.cell(0, 10, u'ตามที่ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ได้ขอรับบริการจัดการเรียนการสอนจาก')
    pdf.ln(8)
    pdf.cell(19, 10, u'')
    pdf.cell(23, 10, u'ท่านในรายวิชา                                                              สำหรับนักศึกษาโครงการพิเศษ (สองภาษา) ')
    pdf.cell(20, 10, u'' + subjectName + '  '  + subjectID) 
    pdf.ln(8)
    pdf.cell(19, 10, u'')
    pdf.cell(0, 10, u'ภาคเรียนที่ .........  นั้น')
    pdf.ln(8)
    pdf.cell(45, 10, u'')
    pdf.cell(0, 10, u'ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ขอให้ท่านยืนยันการจัดการเรียนการสอนในราย')
    pdf.ln(8)
    pdf.cell(19, 0, u'')
    pdf.cell(0, 10, u'วิชาดังกล่าว  ตามแบบฟอร์มด้านล่าง พร้อมตารางสอนและใบเบิกค่าสอนของอาจารย์ผู้สอน  และส่งคืนกลับ ')
    pdf.ln(8)
    pdf.cell(19, 0, u'')
    pdf.cell(0, 10, u'วิภาคชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  เพื่อจะได้ดำเนินการในส่วนที่เกี่ยวข้องต่อไป')
    pdf.ln(8)
    pdf.cell(45, 10, u'')
    pdf.cell(0, 10, u'จึงเรียนมาเพื่อโปรดทราบ')
    pdf.ln(20)
    pdf.cell(94, 10, u'')
    pdf.cell(100, 10, u'(ผู้ช่วยศาสตราจารย์ ดร.นภดล   วิวัชรโกเศศ)')
    pdf.ln(8)
    pdf.cell(94, 10, u'')
    pdf.cell(90, 10, u'หัวหน้าภาควิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    pdf.ln(14)
    pdf.cell(21, 10, u'')
    pdf.cell(0, 10, u'.........................................................................................................................................................................')
    pdf.ln(8)
    pdf.cell(8, 10,u'')
    pdf.cell(30, 10, u'         ชื่อผู้สอน ' + academicPosition + pre_name + firstname + '   '+ lastname + u'            รหัสผู้สอน ' + proID )
    #pdf.cell(80, 10, u'' + academicPosition +pre_name+ firstname + '   '+ lastname)
    #pdf.cell(80, 10, u'' + proID)
    pdf.ln(8)
    pdf.cell(8, 10,u'')
    pdf.cell(30, 10, u'         ภาควิชา')
    pdf.cell(60, 10, u'' + department)
    pdf.cell(20, 10, u'คณะ')
    pdf.cell(20, 10, u'' + faculty)
    pdf.ln(8)
    pdf.cell(8, 10,u'')
    pdf.cell(30, 10, u'         รหัสวิชา')
    pdf.cell(60, 10, u'' +subjectID)
    pdf.cell(20, 10, u'ชื่อวิชา')
    pdf.cell(20, 10, u'' + subjectName) 
    pdf.ln(8)
    pdf.cell(8, 10,u'')
    pdf.cell(30, 10, u'         ตอนเรียน')
    pdf.cell(40, 10, u'' + sec)
    pdf.cell(10, 10, u'วัน')
    pdf.cell(40, 10, u'' + day)
    pdf.cell(15, 10, u'เวลา')
    pdf.cell(20, 10, u'' + str(time)[:5] + u' น.')
    pdf.ln(8)
    pdf.cell(8, 10,u'')
    pdf.cell(0, 10, u'         ได้ดำเนินการจัดการเรียนการสอนเป็น ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                      ภาษาอังกฤษ  ')
    
    pdf.rect(52, 219, 3, 3)
    pdf.ln(8)
    pdf.cell(0, 10, u'                                      ภาษาไทย')
    pdf.rect(52, 227, 3, 3)
    
    pdf.ln(8)
    pdf.cell(94, 10, u'')
    pdf.cell(100, 10, u'ลงชื่อ................................................อาจารย์ผู้สอน ')
    pdf.ln(8)
    pdf.cell(100, 10, u'')
    pdf.cell(110, 10, u''+u'( ' +short_academicPosition + pre_name + firstname +'   '+ lastname+u' )' )
    pdf.ln(8)
    pdf.cell(94, 10, u'')
    pdf.cell(100, 10, u'ลงชื่อ................................................')
    pdf.ln(8)
    pdf.cell(100, 10, u'')
    pdf.cell(110, 10, u'(..............................................) ')
    pdf.ln(8)
    pdf.cell(94, 10, u'')
    pdf.cell(100, 10, u'หัวหน้าภาควิชา' + department)
    pdf.ln(8)

    pdf.output("group3/uni.pdf", 'F')
    
    # next path will open pdf file in new tab on browser.
    with open('group3/uni.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=uni.pdf'
        return response
    pdf.closed
    
def drawAttr(pdf ,start, end, attr=False): # use to draw table for genallpdf()
    Y = [start, end] # line in Y axis draw form top to down.
    if attr:  # draw when it's a attribute in table
        pdf.line(10,Y[0], 288, Y[0])
    pdf.line(10,Y[1], 288, Y[1]) # pdf.line(x1, y1, x2, y2)
    
    pdf.line(10, Y[0], 10, Y[1]) #all of pdf line below use to split column.
    pdf.line(18, Y[0], 18, Y[1])
    pdf.line(63, Y[0], 63, Y[1])
    pdf.line(71, Y[0], 71, Y[1])
    
    pdf.line(88, Y[0], 88, Y[1])
    pdf.line(131,Y[0], 131, Y[1])
    pdf.line(144, Y[0], 144, Y[1])
    
    pdf.line(150,Y[0], 150, Y[1])
    pdf.line(168,Y[0], 168, Y[1])
    pdf.line(180,Y[0], 180, Y[1])
    pdf.line(200,Y[0], 200, Y[1])

    pdf.line(243,Y[0], 243, Y[1])
    pdf.line(263,Y[0], 263, Y[1])
    pdf.line(288,Y[0], 288, Y[1])

def drawAttr2(pdf, start, end, attr=False): # draw  table for houfpdf()
    Y = [start, end]
    if attr:
        pdf.line(10, Y[0], 198, Y[0])
    pdf.line(10,Y[1], 198, Y[1])
    
    pdf.line(10, Y[0], 10, Y[1])
    pdf.line(30, Y[0], 30, Y[1])
    pdf.line(75, Y[0], 75, Y[1])
    pdf.line(94, Y[0], 94, Y[1])
    
    pdf.line(112, Y[0], 112, Y[1])
    pdf.line(150,Y[0], 150, Y[1])
    pdf.line(198, Y[0], 198, Y[1])

def genallpdf(request): # grnerate pdf for show all section data.
    allTeach = Teach.objects.all()
    allsection = Section.objects.all()
    
    ListSec = [] # collect teacher each sectoin because a section has more than a teacher.
    for sec in allsection: # collecting teacher to each section.
        eachSec = []
        for teach in allTeach:
            if teach.section == sec:
                eachSec.append(teach)
        ListSec.append(eachSec)
        
    pdf = FPDF('L', 'mm', 'A4') # start pdf 'L' is landscape.
    pdf.add_page()
    
    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 8)
        
    ganY = [10, 18]
    drawAttr(pdf, ganY[0], ganY[1], True) # call to draw table
    pdf.cell(0, ganY[0], u'ลำดับ              ชื่อ-สกุล                    ตัวย่อ    รหัสวิชา                ชื่อวิชา                      ตอนเรียน  วัน       เวลา       ห้องเรียน  เบอร์โทรศัพท์                   Email                  บ-ช สหกรณ์      หมายเหตุ    ')
    pdf.ln(4) # width:298 height:210
    
    cnt_no = 0 # use to fill in number column.
    cnt_line = 0  # use to calculate next line to draw row of table.
    for sec in ListSec: # drawing table
        cnt_no += 1
        no = str(cnt_no)
        # write no.
        for Prof in sec: # access all teacher in each section
            cnt_line += 1
            
            try:
                first_name = Prof.prof.firstName
                last_name = Prof.prof.lastName
                full_name = first_name + '  ' + last_name
            except:
                full_name = 'None'
                
            try:
                shortname = Prof.prof.shortName
            except:
                shortname = 'None'
                
            try:
                subjectID = Prof.subject.subjectID
            except:
                subjectID = 'None'
                
            try:
                subject = Prof.subject.subjectName
            except:
                subject = 'None'
                
            try:
                section = Prof.section.section
            except:
                section = " "
                
            try:
                day = Prof.section.date
            except:
                day = ' '
            
            try:
                starttime = Prof.section.startTime
            except:
                starttime = 'None'
                
            try:
                room = Prof.section.classroom
            except:
                room = 'None'
                
            try:
                phone_num = Prof.prof.tell
            except:
                phone_num = 'None'
            
            try:
                email = Prof.prof.email
            except:
                email = 'None'
            
            try:
                sahakorn = Prof.prof.sahakornAccount
            except:
                sahakorn = 'None'
                
            pdf.cell(8, 18, no)
            pdf.cell(45, 18,full_name)
            pdf.cell(8, 18, shortname)
            pdf.cell(17, 18, subjectID)
            pdf.cell(45, 18, subject)
            pdf.cell(12, 18, section)
            pdf.cell(7, 18, day)
            pdf.cell(16, 18, str(starttime))
            pdf.cell(12, 18, room)
            pdf.cell(19, 18, phone_num)
            pdf.cell(43, 18, email)
            pdf.cell(29, 18, sahakorn)

            pdf.ln(8)
            if cnt_line % 16 == 0: # check for new pae. I set maximun 16 teachers per a page. 
                drawAttr(pdf, ganY[0]+ (cnt_line*8), ganY[1] + (cnt_line*8), True)
            else:
                drawAttr(pdf, ganY[0]+ (cnt_line*8), ganY[1] + (cnt_line*8))
            no = ''
    
    pdf.ln(8)
    pdf.cell(230, 18, '')
    pdf.cell(230, 18, u'ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ ')
    pdf.ln(8)
    pdf.cell(240, 18, '')
    pdf.cell(240, 18, u'คณะวิศวกรรมศาสตร์ ')
    pdf.ln(8)
    pdf.output("group3/allTeach.pdf", 'F')
    
    with open('group3/allTeach.pdf', 'rb') as pdf: # use to call pdf page in browser.
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=allTeach.pdf'
        return response
    pdf.closed
    
def gen_single_text(pdf, position, text=""): # use to create a single text for only a line.
    pdf.cell(position, 18, u'')
    pdf.cell(position, 18, u'' + text)
    pdf.ln(8)

def hourpdf(request, employeeID): # use to see working of temporary employee.
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    ganY = [46, 54]  # line bettwen collumn.
    
    employeeObj = HourlyEmployee.objects.get(pk=int(employeeID))
    ListWork = employeeObj.work_set.all()
    
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.set_font('THSarabun', '', 16)
    
    gen_single_text(pdf, 65, u'ใบลงเวลาทำงานลูกจ้างชั่วคราวรายชั่วโมง')
    gen_single_text(pdf, 57, u'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ')
    gen_single_text(pdf, 75, u'ชื่อ' + employeeObj.user.firstname_th + '   '+employeeObj.user.lastname_th)
    
    pdf.ln(8)
    pdf.cell(0, 18, u'      วัน                 วันที่ เดือน ปี           เวลาทำงาน  รวมชั่วโมง          ลายมือชื่อ                       หมายเหตุ')
    drawAttr2(pdf, ganY[0], ganY[1], True)
    pdf.ln(12)

    numLine = 0
    payment = 0
    show_payment = 0
    for working in ListWork:
        numLine += 1
        drawAttr2(pdf, ganY[0] + (numLine*8), ganY[1] + (numLine*8))
        if working.day.weekday() == 0:  # geting day to pdf
            pdf.cell(20, 10, u'วันจันทร์')
        elif working.day.weekday() == 1:
            pdf.cell(20, 10, u'วันอังคาร')
        elif working.day.weekday() == 2:
            pdf.cell(20, 10, u'วันพุธ')
        elif working.day.weekday() == 3:
            pdf.cell(20, 10, u'วันพฤหัสบดี')
        elif working.day.weekday() == 4:
            pdf.cell(20, 10, u'วันศุกร์')
        elif working.day.weekday() == 5:
            pdf.cell(20, 10, u'วันเสาร์')
        else:
            pdf.cell(20, 10, u'วันอาทิตย์')
        
        space = 26
        pdf.cell(5, 10, u''+ str(working.releaseDate.day)) # get day
        if working.releaseDate.month == 1:  # get month
            pdf.cell(space, 10, u' มกราคม พ.ศ. ' )
        elif working.releaseDate.month == 2:
            pdf.cell(space, 10, u' กุมภาพันธ์ พ.ศ. ' )
        elif working.releaseDate.month == 3:
            pdf.cell(space, 10, u' มีนาคม พ.ศ. ' )
        elif working.releaseDate.month == 4:
            pdf.cell(space, 10, u' เมษายน พ.ศ. ' )
        elif working.releaseDate.month == 5:
            pdf.cell(space, 10, u' พฤษภาคม พ.ศ. ' )
        elif working.releaseDate.month == 6:
            pdf.cell(space, 10, u' มิถุนายน พ.ศ. ' )
        elif working.releaseDate.month == 7:
            pdf.cell(space, 10, u' กรกฏาคม พ.ศ. ' )
        elif working.releaseDate.month == 8:
            pdf.cell(space, 10, u' สิงหาคม พ.ศ. ' )
        elif working.releaseDate.month == 9:
            pdf.cell(space, 10, u' กันยายน พ.ศ. ' )
        elif working.releaseDate.month == 10:
            pdf.cell(space, 10, u' ตุลาคม พ.ศ. ' )
        elif working.releaseDate.month == 11:
            pdf.cell(space, 10, u' พฤศจิกายน พ.ศ. ' )
        else:
            pdf.cell(space, 10, u' ธันวาคม พ.ศ. ' )
        
        pdf.cell(17, 10, u''+ str(543+int(str(working.releaseDate.year))) )
        pdf.cell(20, 10, u''+ str(working.startTime.hour)+':'+str(working.startTime.minute))
        come_time = str(working.startTime.hour)+':'+str(working.startTime.minute) # time that employee come to work.
        back_time = str(working.endTime.hour)+':'+str(working.endTime.minute) # time that employee go home
        diff_min = int(back_time.split(':')[1]) - int(come_time.split(':')[1])    # calculate differ value of come_time
        diff_hour = int(back_time.split(':')[0]) - int(come_time.split(':')[0])  # calculate differ value of back_time
        if diff_min < 0:
            diff_min = 60 - diff_min
        diff_min_100 = float(str(diff_min))/60
        
        show_payment = show_payment + ( float(diff_hour)+ (float(diff_min)/100) ) 
        pdf.cell(52, 10, u''+ str(diff_hour)+'.'+str(diff_min))
        pdf.cell(90, 10, u''+working.note)
        pdf.ln(8)
        payment = payment + (float(str(diff_min_100)[:4]) + float(diff_hour))
        
    
    index_str = 0
    show_complete_pay = ''
    for i in str(payment)[:4][::-1]:
        index_str = index_str + 1
        if (index_str % 3) == 0:
            show_complete_pay = ',' + i + show_complete_pay 
        else:
            show_complete_pay = i + show_complete_pay 
    
    gen_single_text(pdf, 90, u'รวมจำนวนชั่วโมง ' +str(show_payment)+ u' ชั่วโมง') # call spacial funtion to write a text per line.
    gen_single_text(pdf, 90, u'อัตรา 45.45 บาท ชั่วโมง')
    payment = payment * 45.45
    gen_single_text(pdf, 85, u'รวมเป็นเงินทั้งสิ้น ' + str(payment)[:4] +u' บาท')
    gen_single_text(pdf, 85, u'(                                     )')
    gen_single_text(pdf, 90, u'ได้ตรวจสอบถูกต้องแล้ว')
    gen_single_text(pdf, 65, u'ลงชื่อ........................................................................................')
    gen_single_text(pdf, 70, u'(.....................................................................................)')
    
    pdf.output("group3/hour.pdf", 'F')
    
    with open('group3/hour.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=hour.pdf'
        return response
    pdf.closed

def updateProf(request, teachID):
    if request.method == 'POST':
        # get current Teach object that user want to modifies
        currentTeach = Teach.objects.get(id = teachID)

        # get new data from 'group3/prof2lang_update.html' template
        firstName       = request.POST['firstName']         # 2. get firstName
        lastName        = request.POST['lastName']          # 3. get lastName
        shortName       = request.POST['shortName']         # 4. get shortName
        tell            = request.POST['tell']              # 5. get tell
        email           = request.POST['email']             # 6. get email
        sahakornAccount = request.POST['sahakornAccount']   # 7. get sahakornAccount
        department      = request.POST['department']        # 8. get department
        faculty         = request.POST['faculty']           # 9. get faculty

        # get current Prof2Lang object
        currentProf = Prof2Lang.objects.get(profID = currentTeach.prof.profID)

        # modifiles data
        currentProf.firstName       = firstName
        currentProf.lastName        = lastName
        currentProf.shortName       = shortName
        currentProf.tell            = tell
        currentProf.email           = email
        currentProf.sahakornAccount = sahakornAccount
        currentProf.department      = department
        currentProf.faculty         = faculty

        currentProf.save()  # save Prof2Lang modifiles into database

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))

def updateSubject(request, teachID):
    # get current Teach object that user want to modifies
    currentTeach = Teach.objects.get(id = teachID)

    # get new data from 'group3/prof2lang_update.html' template
    subjectName     = request.POST['subjectName']

    # get current Subject object
    currentSubject = currentTeach.subject
    # modify data
    currentSubject.subjectName = subjectName
    # save Subject modify into database
    currentSubject.save()

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))

def updateSection(request, teachID):
    # get current Teach object that user want to modifies
    currentTeach = Teach.objects.get(id = teachID)

    # get new data from 'group3/prof2lang_update.html' template
    classroom = request.POST['classroom']
    startTime_hour = request.POST['startTime_hour']
    startTime_minute = request.POST['startTime_minute']
    endTime_hour = request.POST['endTime_hour']
    endTime_minute = request.POST['endTime_minute']
    date = request.POST['date']

    # create startTime
    startTime = startTime_hour + ":" + startTime_minute + ":" + "00"
    # create endTime
    endTime = endTime_hour + ":" + endTime_minute + ":" + "00"

    # get current Section Object
    section = currentTeach.section
    # modify data
    section.classroom   = classroom
    section.startTime   = startTime
    section.endTime     = endTime
    section.date        = date

    # save Section modify into database
    section.save()

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))
    
def prof2lang_delete(request, profID): # delete teacher data from index page.
    teachObj = Teach.objects.get(pk= int(profID))
    teachObj.delete()
    teachList = Teach.objects.all()
    template = 'group3/prof2lang_index.html'
    return render(
        request,
        template,
        {'teachList':teachList}
    )

def hour_index(request):
    template = 'group3/hour_index.html'

    return render(request, template,
                      {}
                      )
    
def add_hour_page(request, workID):
    workObj = Work.objects.get(pk=int(workID))
    template = 'group3/add_hour.html'
    return render(request, template, {'work_obj':workObj})
    
def shiftProf(request, teachID):
    if request.method == 'POST':
        # get Teach Object
        currentTeach = Teach.objects.get(id = teachID)

        # get data from 'group3/prof2lang_view.html' template
        profID = request.POST['shift-prof']

        # get Prof2Lang object
        selectProf = Prof2Lang.objects.get(profID = profID)

        # change Prof2Lang object in current Teach object
        currentTeach.prof = selectProf
        # save modify Teach object
        currentTeach.save()

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))

def shiftSubject(request, teachID):
    if request.method == 'POST':
        # get Teach Object
        currentTeach = Teach.objects.get(id = teachID)

        # get data from 'group3/prof2lang_view.html' template
        subjectID = request.POST['shift-subject']
        sectionID = request.POST['shift-subject-section']

        # get Subject object
        selectSubject = Subject.objects.get(subjectID = subjectID)
        # get Section object
        selectSection = Section.objects.get(id = int(sectionID))

        # change Subject and Section object in current Teach object
        currentTeach.subject = selectSubject
        currentTeach.section = selectSection
        # save modify Teach object
        currentTeach.save()

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))

def shiftSection(request, teachID):
    if request.method == 'POST':
        # get Teach Object
        currentTeach = Teach.objects.get(id = teachID)

        # get data from 'group3/prof2lang_view.html' template
        sectionID = request.POST['shift-section']

        # get Section object
        selectSection = Section.objects.get(id = int(sectionID))

        # change Section object in current Teach object
        currentTeach.section = selectSection
        # save modify Teach object
        currentTeach.save()

    return HttpResponseRedirect(reverse('group3:prof2lang_view', args=[teachID]))

def search_hour_worker(request):
    if request.method == 'POST':
        name = request.POST["username"]
        try:
            template = "group3/hour_profile.html"
            context = {}
            user = User.objects.get(username=name)
            profile = UserProfile.objects.get(user=user)
            try:    
                worker = HourlyEmployee.objects.get(user=profile)
            except:
                worker = HourlyEmployee(user=profile, employmentRate=45.45)
                worker.save()
            return HttpResponseRedirect(reverse("group3:returnsearch", args=[worker.id]))
        except:
            template = "group3/hour_index.html"
            context = {}
            context["error"] = "โปรดตรวจสอบ username ใหม่อีกครั้ง"
            
        return render(
            request,
            template,
            context
        )

def returnsearch(request, id):
    template = "group3/hour_profile.html"
    context = {}
    worker = HourlyEmployee.objects.get(id=int(id))
    ListWork = worker.work_set.all().order_by('id')
    print ListWork[0].releaseDate
    try:
        profile = worker.user

        context['name_th'] = profile.firstname_th
        context['last_th'] = profile.lastname_th
        context['name_en'] = profile.firstname_en
        context['last_en'] = profile.lastname_en

        if profile.department == '0':
            department = ''
        elif profile.department == '1':
            department = 'วิศวกรรมไฟฟ้าและคอมพิวเตอร์'

        context['department'] = department

        if profile.faculty == '0':
            faculty = ''
        elif profile.faculty == '1':
            faculty = 'วิศวกรรมศาสตร์'

        context['faculty'] = faculty
        context['tel'] = profile.tel
        context['worker'] = worker

        if str(ListWork[len(ListWork)-1].endTime) == time.strftime("00:00:01"):
            status_on = 'disabled'
            status_off = 'active'
        else:
            status_on = 'active'
            status_off = 'disabled'

        context['ListWork'] = ListWork
        context['employObj'] = worker
        context['status_on'] = status_on
        context['status_off'] = status_off

    except:
        print "Except"
        context['ListWork'] = ListWork
        context['employObj'] = worker
        context['status_on'] = 'active'
        context['status_off'] = 'disabled'

    return render(
        request,
        template,
        context
    )

def add_hour_note(request, workID):
    if request.method == 'POST':
        workObj = Work.objects.get(id=int(workID))
        workObj.note = request.POST['input_note_hour']
        workObj.save()
        employee = workObj.employee
        return HttpResponseRedirect(reverse('group3:returnsearch', args=[employee.id]))

def add_hour_date(request, employeeID):
    employee = HourlyEmployee.objects.get(id=employeeID)
    userprofile = employee.user
    emploeeObj = HourlyEmployee.objects.get(user=userprofile)
    workObj = Work(employee=emploeeObj, startTime=time.strftime("%H:%M"), endTime=time.strftime("00:00:01"))
    workObj.save()
    return HttpResponseRedirect(reverse('group3:returnsearch', args=[employeeID]))

def add_hour_date2(request, employeeID):
    employee = HourlyEmployee.objects.get(id=employeeID)
    userprofile = employee.user
    emploeeObj = HourlyEmployee.objects.get(user=userprofile)
    lenworkObj = len(Work.objects.filter(employee=emploeeObj)) - 1
    workObj = Work.objects.filter(employee=emploeeObj)[lenworkObj]
    workObj.endTime = endTime=time.strftime("%H:%M")
    workObj.save()
    return HttpResponseRedirect(reverse('group3:returnsearch', args=[employeeID]))


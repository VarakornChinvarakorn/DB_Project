#-*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from login.models import UserProfile
import django.shortcuts

from group3.models import *
from django.http import HttpResponse
from fpdf import FPDF
# Create your views here.
def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user = user)
        return userprofile.type
    except:
        return 'admin'

def prof2lang_index(request):
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
    
    pdf.image('group3/trarachakarn.png',20,20,20)   # insert image
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
    try: # check all data for beware blank data.
        proID = teachObj.prof.profID
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
    pdf.set_font('THSarabun Bold', '', 18)  
    pdf.cell(0, 10, u'                         บันทึกข้อความ')
    pdf.ln(10)
    pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)  # thai font
    pdf.set_font('THSarabun', '', 16)
    pdf.cell(0, 10, u'         ส่วนราชการ ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ คณะวิศวกรรมศาสตร์  โทร. ๘๕๑๘')
    pdf.line(46,52,180,52)
    pdf.ln(8)
    pdf.cell(0, 10, u'         ที่                                                    วันที่  ')
    pdf.line(30,60,180,60)
    pdf.ln(8)
    pdf.cell(0, 10, u'         เรื่อง การจัดการเรียนการสอนสำหรับนักศึกษาโครงการพิเศษ(สองภาษา) ')
    pdf.line(30,68,180,68)
    pdf.ln(8)
    pdf.cell(0, 10, u'         เรียน หัวหน้าภาควิชา ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                     ตามที่ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ได้ขอรับบริการจัดการเรียนการสอนจากท่านในราย')
    pdf.ln(8)
    pdf.cell(20, 10, u'         วิชา                                                                 สำหรับนักศึกษาโครงการพิเศษ (สองภาษา) ')
    pdf.cell(20, 10, u'' + subjectName + '  '  + subjectID) 
    pdf.ln(8)
    pdf.cell(0, 10, u'         ภาคเรียนที่ .........  นั้น')
    pdf.ln(8)
    pdf.cell(0, 10, u'                    ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ขอให้ท่านยืนยันการจัดการเรียนการสอนในรายวิชาดังกล่าว')
    pdf.ln(8)
    pdf.cell(0, 10, u'         ตามแบบฟอร์มด้านล่าง พร้อมตารางสอนและใบเบิกค่าสอนของอาจารย์ผู้สอนและส่งคืนกลับภาควิชาวิศวกรรม ')
    pdf.ln(8)
    pdf.cell(0, 10, u'         ไฟฟ้าและคอมพิวเตอร์  เพื่อจะได้ดำเนินการในส่วนที่เกี่ยวข้องต่อไป')
    pdf.ln(8)
    pdf.cell(0, 10, u'                        จึงเรียนมาเพื่อโปรดทราบ')
    pdf.ln(20)
    pdf.cell(100, 10, u'')
    pdf.cell(100, 10, u'(ดร.นภดล   วิวัชรโกเศศ)')
    pdf.ln(8)
    pdf.cell(90, 10, u'')
    pdf.cell(90, 10, u'หัวหน้าภาควิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    pdf.ln(14)
    pdf.cell(0, 10, u'            .........................................................................................................................................................................')
    pdf.ln(8)
    pdf.cell(30, 10, u'         ชื่อผู้สอน                                                    รหัสผู้สอน')
    pdf.cell(80, 10, u'' + firstname + '   '+ lastname)
    pdf.cell(80, 10, u'' + proID)
    pdf.ln(8)
    pdf.cell(30, 10, u'         ภาควิชา')
    pdf.cell(60, 10, u'' + department)
    pdf.cell(20, 10, u'คณะ')
    pdf.cell(20, 10, u'' + faculty)
    pdf.ln(8)
    pdf.cell(30, 10, u'         รหัสวิชา')
    pdf.cell(60, 10, u'' +subjectID)
    pdf.cell(20, 10, u'ชื่อวิชา')
    pdf.cell(20, 10, u'' + subjectName) 
    pdf.ln(8)
    pdf.cell(30, 10, u'         ตอนเรียน')
    pdf.cell(40, 10, u'' + sec)
    pdf.cell(10, 10, u'วัน')
    pdf.cell(40, 10, u'' + day)
    pdf.cell(15, 10, u'เวลา')
    pdf.cell(20, 10, u'' + time)
    pdf.ln(8)
    pdf.cell(0, 10, u'         ได้จัดการเรียนการสอนเป็น ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                           ภาษาอังกฤษ  ')
    
    pdf.rect(37, 219, 3, 3)
    pdf.ln(8)
    pdf.cell(0, 10, u'                           ภาษาไทย')
    pdf.rect(37, 227, 3, 3)
    
    pdf.ln(8)
    pdf.cell(100, 10, u'')
    pdf.cell(100, 10, u'ลงชื่อ......................................อาจารย์ผู้สอน ')
    pdf.ln(8)
    pdf.cell(110, 10, u'')
    pdf.cell(110, 10, u'(..............................................) ')
    pdf.ln(8)
    pdf.cell(110, 10, u'')
    pdf.cell(110, 10, u'ลงชื่อ......................................')
    pdf.ln(8)
    pdf.cell(110, 10, u'')
    pdf.cell(110, 10, u'(..............................................) ')
    pdf.ln(8)
    pdf.cell(100, 10, u'')
    pdf.cell(100, 10, u'หัวหน้าภาควิชา............................................')
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
    pdf.line(105, Y[0], 105, Y[1])
    
    pdf.line(130, Y[0], 130, Y[1])
    pdf.line(163,Y[0], 163, Y[1])
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
            pdf.cell(45, 18, full_name)
            pdf.cell(8, 18, shortname)
            pdf.cell(17, 18, subjectID)
            pdf.cell(45, 18, subject)
            pdf.cell(12, 18, section)
            pdf.cell(7, 18, day)
            pdf.cell(17, 18, str(starttime))
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

def hourpdf(request): # use to see working of temporary employee.
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    ganY = [46, 54]  # line bettwen collumn.
    
    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 12)
    
    gen_single_text(pdf, 60, u'ใบลงเวลาทำงานลูกจ้างชั่วคราวรายชั่วโมง')
    gen_single_text(pdf, 45, u'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ')
    gen_single_text(pdf, 70, u'ชื่อ')
    
    pdf.ln(8)
    pdf.cell(0, 18, u'    วัน           วันที่ เดือน ปี          เวลาทำงาน      รวมชั่วโมง       ลายมือชื่อ          หมายเหตุ')
    drawAttr2(pdf, ganY[0], ganY[1], True)
    
    gen_single_text(pdf, 90, u'รวมจำนวนชั่วโมง ' + u'ชั่วโมง') # call spacial funtion to write a text per line.
    gen_single_text(pdf, 90, u'อัตรา 45.45 บาท ชั่วโมง')
    gen_single_text(pdf, 90, u'รวมเป็นเงินทั้งสิ้น' + u'บาท')
    gen_single_text(pdf, 90, u'(                   )')
    gen_single_text(pdf, 90, u'ได้ตรวจสอบถูกต้องแล้ว')
    gen_single_text(pdf, 75, u'ลงชื่อ.......................................................')
    gen_single_text(pdf, 80, u'(...................................................)')
    
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
    return render(request, template)

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
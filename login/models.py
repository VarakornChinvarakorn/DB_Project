#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)                                           # 1. user

    # The additional attributes we wish to include.
    website         = models.URLField(blank=True)                               # 2. website
    picture         = models.ImageField(upload_to='profile_images', blank=True) # 3. picture
    firstname_th    = models.CharField(max_length=100)                          # 4. first name in Thai
    lastname_th     = models.CharField(max_length=100)                          # 5. last name in Thai
    firstname_en    = models.CharField(max_length=100)                          # 6. first name in English
    lastname_en     = models.CharField(max_length=100)                          # 7. last name in English
    address         = models.TextField()                                        # 8. address
    office          = models.TextField()                                        # 9. office
    tel             = models.CharField(max_length=20)                           # 10. telephone number
    ext             = models.CharField(max_length=10, blank=True)               # 11. ต่อ สำหรับเบอร์โทร
    departmentChoices = (
        ('0', ''),
        ('1', 'วิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    )
    department      = models.CharField(max_length=1, choices=departmentChoices) # 12. department

    facultyChoices = (
        ('0', ''),
        ('1', 'วิศวกรรมศาสตร์')
    )
    faculty         = models.CharField(max_length=1, choices=facultyChoices)    # 13. faculty

    typeChoices = (
        ('0', 'Student'),
        ('1', 'Teacher'),
        ('2', 'Officer')
    )
    type            = models.CharField(max_length=1, choices=typeChoices)       # 14. type of user

    prefix_name_choices = (
        ('0', 'นาย'),       # Mr.
        ('1', 'นาง'),       # Mrs.
        ('2', 'นางสาว'),    # Miss.
        ('3', 'ดร.')        # Dr.
    )
    prefix_name  = models.CharField(max_length=1, choices=prefix_name_choices)  # 15. คำนำหน้าชื่อ
    
    # Override the __unicode__() method to return out something meaningful!
    #def __unicode__(self):
    #    return self.user.username
    
    def __unicode__(self):
        if self.prefix_name == '0':
            prefix = 'Mr.'
        elif self.prefix_name == '1':
            prefix = 'Mrs.'
        elif self.prefix_name == '2':
            prefix = 'Miss.'
        elif self.prefix_name == '3':
            prefix = 'Dr.'
        else:
            prefix = ''
        return prefix + self.firstname_en + " " + self.lastname_en

class Student(models.Model):
    userprofile = models.OneToOneField(UserProfile)                 # 1. user profile
    std_id = models.CharField(max_length=13)                        # 2. student id
    schemeChoices = (
        ('0', 'หลักสูตรปรับปรุง Cpr.E 54'),
        ('1', 'หลักสูตรปรับปรุง EE 51'),
        ('2', 'หลักสูตรปรับปรุง ECE 55'),
        ('3', 'หลักสูตรมหาบัณฑิต 55'),      # ของ ป.โท
        ('4', 'หลักสูตรดุษฎีบัณฑิต 55')       # ของ ป.เอก
    )
    scheme = models.CharField(max_length=1, choices=schemeChoices)  # 3. scheme หลักสูตร

    mainChoices = (
        ('0', 'Cpr.E'),
        ('1', 'G'),
        ('2', 'U'),
        ('3', 'C')
    )
    main = models.CharField(max_length=1, choices=mainChoices)      # 4. main สาขา

    sexChoices = (
        ('0', 'ชาย'),
        ('1', 'หญิง')
    )
    sex = models.CharField(max_length=1, choices=sexChoices)        # 5. sex เพศ

    degreeChoices = (
        ('0', 'ปริญญาตรี'),
        ('1', 'ปริญญาโท'),
        ('2', 'ปริญญาเอก')
    )
    degree = models.CharField(max_length=1, choices=degreeChoices)  # 6. degree ระดับการศึกษา
    id_number = models.CharField(max_length=13)                     # 7. เลขประจำตัวประชาชน
    nationality = models.CharField(max_length=50)                   # 8. เชื้อชาติ
    religion = models.CharField(max_length=50)                      # 9. ศาสนา

    bloodTypeChoices = (
        ('0', 'O'),
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'AB')
    )
    blood_type = models.CharField(max_length=2, choices=bloodTypeChoices)   # 10. หมู่เลือด
    birthDate = models.DateField()                                          # 11. วันเกิด
    
    def __unicode__(self):
        return self.userprofile.firstname_en + " " + self.userprofile.lastname_en

class Teacher(models.Model):
    userprofile = models.OneToOneField(UserProfile) # 1. user profile
    shortname = models.CharField(max_length=3)      # 2. short name ตัวย่อชื่อ
    positionChoices = (
        ('0', 'ข้าราชการ'),
        ('1', 'ลูกจ้างประจำ'),
        ('2', 'ข้าราชการบำนาญ'),
        ('3', 'พนักงานมหาวิทยาลัย')
    )
    position = models.CharField(max_length=1, choices=positionChoices)     # 3. ตำแหน่ง

    academic_position_choice = (
        ('0', ''),
        ('1', 'ผู้ช่วยศาสตราจารย์'),    # ตัวย่อไทย ผศ.  ตัวย่อแบบอเมริกา  Asst.Prof.   มาจาก Assistant Professor
        ('2', 'รองศาสตราจารย์'),     # ตัวย่อไทย รศ.  ตัวย่อแบบอเมริกา  Assoc.Prof.  มาจาก Associate Professor
        ('3', 'ศาสตราจารย์')          # ตัวย่อไทย ศ.   ตัวย่อแบบอเมริกา Prof.         มาจาก Professor
    )
    academic_position = models.CharField(max_length=1, choices=academic_position_choice)    # 4. ตำแหน่งทางวิชาการ
    
    def __unicode__(self):
        return self.userprofile.firstname_en + " " + self.userprofile.lastname_en

class Officer(models.Model):
    userprofile = models.OneToOneField(UserProfile) # 1. user profile
    positionChoices = (
        ('0', 'ข้าราชการ'),
        ('1', 'ลูกจ้างประจำ'),
        ('2', 'ข้าราชการบำนาญ'),
        ('3', 'พนักงานมหาวิทยาลัย')
    )
    position = models.CharField(max_length=1, choices=positionChoices)     # 2. ตำแหน่ง
    
    def __unicode__(self):
        return self.userprofile.firstname_en + " " + self.userprofile.lastname_en

#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from login.forms import *
from login.models import *
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def index(request):
    template = 'login/index.html'
    context = RequestContext(request)
    registered = False
    errors=[]

    if request.method == 'POST':
        users = User.objects.all()  # get all User objects
        # get data from register_form
        username = request.POST['username']     # get username
        first_name = request.POST['first_name'] # get first name
        last_name = request.POST['last_name']   # get last name
        email = request.POST['email']           # get email
        password = request.POST['password']     # get password
        check_password = request.POST['check_password'] # get check_password
        if password != check_password:
            print 'password incorrected'
            errors.append(1)            # show some error message in template
        else:
            print 'password corrected'
            for user in users:                  # check user is duplicate
                if(username == user.username):
                    errors.append(2)    # show some error message in template
                    break
            if len(errors)==0:
                print'can save user'
                # create new User object and save in database
                new_user = User(username=username,
                                first_name=first_name,
                                last_name=last_name,
                                email=email)
                new_user.set_password(password)
                new_user.save()

                # create new UserProfile object and save in database
                new_profile = UserProfile()
                new_profile.user = new_user
                new_profile.save()
                # change state registered in template was success
                registered = True

    return render_to_response(
        template,
        {'registered': registered, 'errors': errors},
        context)

def menu(request):
    template = 'login/menu.html'
    context = RequestContext(request)

    return  render_to_response(
        template,
        {},
        context
    )

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'login/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('login:menu'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('login/login.html', {'error':'error'}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('login:index'))

def user_register(request):
    template = 'login/register.html'
    context = {}
    errors = []

    if request.method == 'POST':
        # get all User objects
        users = User.objects.all()

        # get data from template login/register.html
        username        = request.POST['username']          # get 1. username
        std_id          = request.POST['std_id']            # get 2. std_id
        firstname_th    = request.POST['firstname_th']      # get 3. firstname_th
        lastname_th     = request.POST['lastname_th']       # get 4. lastname_th
        firstname_en    = request.POST['firstname_en']      # get 5. firstname_en
        lastname_en     = request.POST['lastname_en']       # get 6. lastname_en
        address         = request.POST['address']           # get 7. address
        office          = request.POST['office']            # get 8. office
        email           = request.POST['email']             # get 9. email
        tel             = request.POST['tel']               # get 10. tel
        ext             = request.POST['ext']               # get 11. ext
        scheme          = request.POST['scheme']            # get 12. scheme
        main            = request.POST['main']              # get 13. main
        department      = request.POST['department']        # get 14. department
        faculty         = request.POST['faculty']           # get 15. faculty
        sex             = request.POST['sex']               # get 16. sex
        degree          = request.POST['degree']            # get 17. degree
        id_number       = request.POST['id_number']         # get 18. id_number
        nationality     = request.POST['nationality']       # get 19. nationality
        religion        = request.POST['religion']          # get 20. religion
        blood_type      = request.POST['blood_type']        # get 21. blood_type
        birthDate       = request.POST['birthDate']         # get 22. birthDate
        prefix_name     = request.POST['prefix_name']       # get 23. prefix_name
        password        = request.POST['password']          # get 24. password
        check_password  = request.POST['check_password']    # get 25. check_password

        # errors 1: User fill invalid password
        if password != check_password:
            print 'password is invalid'
            errors.append(1)

        # errors 2: username is duplicate
        try:
            user = User.objects.get(username = username)
            errors.append(2)
        except:
            pass

        # errors 3: std_id is duplicate
        try:
            std = Student.objects.get(std_id = std_id)
            errors.append(3)
        except:
            pass

        # errors 4: id_number is duplicate
        try:
            std = Student.objects.get(id_number = id_number)
            errors.append(4)
        except:
            pass

        # if don't have an error
        if len(errors) == 0:
            # create new User object
            newUser = User(
                username        = username,
                first_name      = firstname_en,
                last_name       = lastname_en,
                email           = email
            )
            newUser.set_password(password)
            newUser.save()  # save new User object into database

            # create new UserProfile object
            newUserProfile = UserProfile(
                user            = newUser,          # set 1. user
                # set 2. website
                # set 3. picture
                firstname_th    = firstname_th,     # set 4. first name in Thai
                lastname_th     = lastname_th,      # set 5. last name in Thai
                firstname_en    = firstname_en,     # set 6. first name in English
                lastname_en     = lastname_en,      # set 7. last name in English
                address         = address,          # set 8. address
                office          = office,           # set 9. office
                tel             = tel,              # set 10. telephone number
                ext             = ext,              # set 11. ต่อ สำหรับเบอร์โทร
                department      = department,       # set 12. department
                faculty         = faculty,          # set 13. faculty
                type            = '0',              # set 14. type '0' is Student
                prefix_name     = prefix_name       # set 15. prefix_name
            )
            newUserProfile.save() # save new UserProfile object into database

            # create new Student object
            newStudent = Student(
                userprofile     = newUserProfile,   # set 1. user profile
                std_id          = std_id,           # set 2. student id
                scheme          = scheme,           # set 3. scheme หลักสูตร
                main            = main,             # set 4. main สาขา
                sex             = sex,              # set 5. sex
                degree          = degree,           # set 6. degree
                id_number       = id_number,        # set 7. เลขประจำตัวประชาชน
                nationality     = nationality,      # set 8. เชื้อชาติ
                religion        = religion,         # set 9. ศาสนา
                blood_type      = blood_type,       # set 10. หมู่เลือด
                birthDate       = birthDate         # set 11. วันเกิด
            )
            newStudent.save() # save new Srudent object into database

            # redirect to template with register is success
            context['registered'] = True
        # if have an error
        else:
            # redirect to template with errors list
            context['errors'] = errors

            # redirect to template with some data
            context['username']     = username
            context['std_id']       = std_id
            context['firstname_th'] = firstname_th
            context['lastname_th']  = lastname_th
            context['firstname_en'] = firstname_en
            context['lastname_en']  = lastname_en
            context['address']      = address
            context['office']       = office
            context['email']        = email
            context['tel']          = tel
            context['ext']          = ext
            context['id_number']    = id_number
            context['nationality']  = nationality
            context['religion']     = religion
            context['birthDate']    = birthDate

            # delete some context dict that user fill invalid
            for error in errors:
                if error == 2:
                    del context['username']
                elif error == 3:
                    del context['std_id']
                elif error == 4:
                    del context['id_number']

    return render(
        request,
        template,
        context
    )

def testDateField(request):
    template = 'login/test_date_field.html'
    context = {}

    if request.method == 'POST':
        date = request.POST['date']     # ตัวที่ได้มาจากหน้าเว็บรูปแบบจะเป็น วัน-เดือน-ปี

        # ทำการแปลงให้เป็น ปี-เดือน-วัน แล้วเป็นเป็นตัวแปรประเภท datetime.date ให้พร้อมสำหรับบันทึกลง database
        valid_date = datetime.strptime(date, '%d-%m-%Y').date()
        print ">>> ", valid_date, " ", type(valid_date), " <<<"

    return render(
        request,
        template,
        context
    )
from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.contrib import messages

from basic_app.forms import UserProfileInfoForm,UserForm
from basic_app.models import UserProfileInfo
#for login system.. importing....
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,DetailView
from epr_app.models import mst_patient,appt_doctor
from epr_app.models import mst_specialization
from basic_app import forms
# Create your views here.

# def index(request):
#     return render(request,'basic_app/index.html')

def spcl_surgeon(request):
    return render(request,'basic_app/spcl1.html')

def spcl_ent(request):
    return render(request,'basic_app/ent.html')

def spcl_gynae(request):
    return render(request,'basic_app/gyn.html')

def spcl_gen_phy(request):
    return render(request,'basic_app/gen_phy.html')


def base(request):
    return render(request,'basic_app/base.html')

@login_required
def special(request):
    #Remember to also set login url in settings.py
    #LOGIN_URL='basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    #log out the user
    logout(request)
    #return to homepage
    return HttpResponseRedirect(reverse('index'))

def registration(request):

    registered=False

    if request.method=='POST':

        #Get info from "both" forms
        #It appears as one form to the user on the .html page
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        #Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            #Save User Form to Database
            user=user_form.save()

            #Hash the password
            user.set_password(user.password)

            #Update with Hashed set_password
            user.save()

            #Now we deal with extra info!

            #Can't commit yet because we still need to manipulate
            profile=profile_form.save(commit=False)

            #Set one to one relationship between
            #userform and UserProfileInfoForm
            profile.user=user

            #Check if they provided a profile picture

            #Now we save model
            profile.save()

            #Registration Successful!
            registered=True

        else:
            #One of the forms was invalid if this else gets called
            print(user_form.errors,profile_form.errors)
    else:
        #Was not an HTTP post so we just render the forms as blankself.
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    #This is the render and context dictionary to feed
    #back to the registration.html file page

    return render(request,'basic_app/registration.html',
                                {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered })

def user_login(request):
    if request.method == 'POST':
        #first get the username and password supplied
        username=request.POST.get('username')
        password=request.POST.get('password')
        #django's buil-in authentication function:

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:

                #login the user
                login(request,user)
                #send the user back to some page
                #in this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                #if acc is not active:
                return HttpResponse("Your account is not active")
        else:
            print("Someone tried to loin and failed")
            print("they used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        #Nothing has been provided for username or password.
        return render(request,'basic_app/login.html',{})

@login_required
def profile(request):
    hii=UserProfileInfo.objects.all()
    print(hii)
    username = None
    if request.user.is_authenticated():
        username =request.user.username
        email =request.user.email
        first_name =request.user.first_name
        last_name =request.user.last_name
        pro=UserProfileInfo.objects.filter(user=request.user.id);
        for p in pro:
            print(p.address,p.dob,p.pincode,p.phone);
        print(username)
        print(email)

        print(first_name)
        print(last_name)
        return render(request,'basic_app/profile.html',{'p':p,'username' : username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'hii':hii})


def prsc(request):
    patient = forms.User.objects.get(username=request.user)
    print(patient)
    patient = mst_patient.objects.filter(user_id=patient)
    print(patient)

    # if request.user.is_authenticated():
    # if request.user.is_authenticated():
    #     # p_id = request.user.p_id
    #     fname = request.user.p_fname
    #     desc = request.user.prob_des
    #
    #     return render(request,'basic_app/prescriptions.html',{'patient':patient,'p_id':p_id,'fname':fname,
    #                                                         'desc':desc})

    return render(request,'basic_app/prescription_detail.html',{'prsc':patient})

def appointment(request):
    user_id = forms.User.objects.get(username = request.user)
    print(user_id)
    patient = appt_doctor.objects.filter(user = user_id)
    print(patient)

    return render(request,'basic_app/appointment_detail.html',{'appt':patient})



def search(request):
    if request.method == 'POST':
        search_bar = request.POST['search']

        if search_bar:
            match = mst_specialization.objects.filter(Q(sp_name__icontains=search_bar) |
                                                       Q(d_name__icontains=search_bar)
                                                         )
            match2 = mst_patient.objects.filter(Q(p_fname__icontains=search_bar))
            if match or match2:
                return render(request,'basic_app/search.html',{'result':match,'result1':match2})
            else:
                messages.error(request,'Sorry! No such results found!')
        else:
            return HttpResponseRedirect('basic_app/search/')

    return render(request,'basic_app/search.html')

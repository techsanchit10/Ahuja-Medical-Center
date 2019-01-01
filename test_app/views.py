# Create your views here.
from django.shortcuts import render

# Create your views here.
# from basic_app.forms import UserProfileInfoForm,UserForm

#for login system.. importing....
from doctors_app.models import UserProfileInfo
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# def index1(request):
#     return HttpResponse('this is index page')

def lab_login(request):
    return render(request,'hospital_temp/login.html')

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
                # return HttpResponseRedirect('doctor_pt')
                return render(request,"hospital_temp/dp.html")
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

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from appointment.forms import AppointmentModelForm,PIDForm
from epr_app.models import appt_doctor,transaction_appt
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from appointment import forms
# from django.http import HttpResponseRedirect
# from django.urls import reverse
import datetime
from django.core.mail import EmailMessage


# disabling csrf (cross site request forgery)

@login_required
def book_patient(request):
    registered = False
    user = forms.User.objects.get(username = request.user)
    print(user)
    count = appt_doctor.objects.count()
    # p_id = count + 1
    app_no = count + 1
    if request.method == 'POST':
        pid_form = PIDForm(data = request.POST)
        appt_form = AppointmentModelForm(data=request.POST)

        print(appt_form)

        print("Hello")

        if pid_form.is_valid() and appt_form.is_valid():
            print("hi")

            appt = appt_form.save(commit = False)
            appt.user = user
            appt.app_no = app_no
            appt.save()
            registered = True
            email = EmailMessage('Appointment Recieved', "Hello Dr. There is an appointment for you! ",  to=['mokshnarang22@gmail.com','kanwal.badshah@gmail.com'])
            email.send()
            return render(request,'appointment/after_appt.html',{'p_id':appt.p_id,'app_no':appt.app_no,'date':appt.appt_date})

    else:
        pid_form = PIDForm()
        appt_form = AppointmentModelForm()


    context_d = {
                'pid_form':pid_form,
                'appt_form':appt_form,
                'app_no':app_no
                }
        # print(request.POST)
    return render(request,'appointment/appt.html',context=context_d)

from django.shortcuts import render,redirect
from django.http import HttpResponse
from epr_app.forms import PatientForm,ExistPatientForm,PIDForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import mst_patient
from epr_app import forms
import random
from django.core.mail import EmailMessage


# Create your views here.
@login_required
def epr_register(request):
    registered = False
    # id = mst_patient.p_id
    user_id = forms.User.objects.get(username=request.user)
    count = mst_patient.objects.count()

    p_id = count+1
    # print(id)

    if request.method == 'POST':

        patient_form = PatientForm(data=request.POST)

        print("hello1")
        print(patient_form)
        print(p_id)
        if patient_form.is_valid():
            print("chi")

            patient = patient_form.save(commit=False)
            patient.user_id = user_id
            patient.p_id = p_id
            patient.save()

            registered = True
            email = EmailMessage('E-prescription Request Recieved', "Hello Dr. There is an ePrescription request! You can check it in your Doctor profile section! ", to=['mokshnarang22@gmail.com','kanwal.badshah@gmail.com'])
            email.send()

            return render(request,'epr_app/after_prsc.html',{'p_fname':patient.p_fname,'p_id':p_id,'prob_des':patient.prob_des})

    else:
        patient_form = PatientForm()
        registered = True


    # print(request.POST)
    my_dict = {'patient_form':patient_form,
                'registered':registered,
                'p_id': p_id,
                }

    return render(request,'epr_app/eprsc2.html',context = my_dict)


@login_required
def exist_epr_register(request):
    registered = False

    # name = mst_patient.objects.get(p_fname = mst_patient.p_id)


    if request.method == 'POST':
        pid_form = PIDForm(data = request.POST)
        e_patient_form = ExistPatientForm(data=request.POST)
        print("hello1")
        print(pid_form)
        print(e_patient_form)


        if pid_form.is_valid() and e_patient_form.is_valid():
            print("chi")

            e_patient = e_patient_form.save(commit=False)
            e_patient.save()

            registered = True
            email = EmailMessage('E-prescription Request Recieved', "Hello Dr. There is an ePrescription request! You can check it in your Doctor profile section! ", to=['mokshnarang22@gmail.com','kanwal.badshah@gmail.com'])
            email.send()
            return render(request,'epr_app/after_prsc.html',{'p_id':e_patient.p_id,'prob_des':e_patient.prob_des})

    else:
        pid_form = PIDForm()
        e_patient_form = ExistPatientForm()

        registered = True

    # print(request.POST)
    my_dict = { 'pid_form':pid_form,
                'e_patient_form':e_patient_form,
                'registered':registered,
                # 'id': p_id
                }

    return render(request,'epr_app/exist_eprsc.html',context = my_dict)

from django import forms
from django.forms import extras
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.models import User
from epr_app.models import appt_doctor


class AppointmentModelForm(forms.ModelForm):
    user = forms.CharField(required = False)
    phone = forms.CharField(required = False)

    class Meta():
        model=appt_doctor
        # fields=('p_id','app_no','p_fname','p_lname','email','address','pincode','date_of_birth','sp_name','d_name')
        # fields = '__all__'
        exclude = ['user',]



class PIDForm(forms.ModelForm):
    class Meta():
        model=appt_doctor
        fields = ('p_id',)

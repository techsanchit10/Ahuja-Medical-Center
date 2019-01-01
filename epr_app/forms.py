from django import forms
from django.contrib.auth.models import User
from epr_app.models import mst_patient,mst_doctor,mst_specialization,exist_patient
# exist_patient


class PatientForm(forms.ModelForm):
    user_id = forms.CharField(required=False)
    # username = forms.CharField(required=False)
    # sp_name = forms.ChoiceField(required=False)
    # d_id1 =
    # d_name =
    # prob_des = forms.CharField( widget = forms.Textarea)


    class Meta():
        model = mst_patient
        # fields = '__all__'
        exclude = ['d_id1','user_id','pres']
        # exclude = '__all__'

class ExistPatientForm(forms.ModelForm):
    prob_des = forms.CharField( widget = forms.Textarea)

    class Meta():
        model = exist_patient
        exclude = ['pres',]

class PIDForm(forms.ModelForm):
    class Meta():
        model=exist_patient
        fields = ('p_id',)

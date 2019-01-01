from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from  django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    if value.isalpha() != 1:
        raise ValidationError(
        _('%(value)s Name can only be Alphabets!'),
        params={'value':value},
        )
def validate_pass(value):
    if len(value)<=8:
        raise ValidationError(
        _('%(value)s Enter 8 values '),
        params={'value':value},
        )

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(),validators=[validate_pass])

    first_name=forms.CharField(validators=[validate_name])
    last_name=forms.CharField(validators=[validate_name])
    class Meta():
        model=User
        fields=('username','email','password','first_name','last_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('dob','address','phone','pincode')

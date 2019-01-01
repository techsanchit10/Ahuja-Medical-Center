from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from  django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(value):
    if len(value) !=10:
        raise ValidationError(
        _('%(value)s - Phone number cannot be less than 10 digits!'),
        params={'value':value},
        )
        
def validate_number1(value):
    if len(value) !=6:
        raise ValidationError(
        _('%(value)s - Pincode should be of 6 characters only!'),
        params={'value':value},
        )

# Create your models here.



class UserProfileInfo(models.Model):

    #Create relationship
    user=models.OneToOneField(User)

    #Add any additional attributes you wantdob = models.DateField()

    dob = models.DateField()
    address = models.CharField(max_length = 200)
    phone = models.CharField(max_length=10, validators=[validate_number])
    pincode = models.CharField(max_length=6, validators=[validate_number1])
    test =models.CharField(max_length = 200, blank=True)

    def __str__(self):
        #Built-in attribute of django.contrib.auth.models.User!
        return self.user.username

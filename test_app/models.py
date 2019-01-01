from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo_t(models.Model):

    #Create relationship
    user=models.OneToOneField(User)

    doctors_appt = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.doctors_appt

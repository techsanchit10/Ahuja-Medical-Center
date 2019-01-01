from django.conf.urls import url,include
from django.contrib import admin

#importing views

from appointment import views

app_name = 'appointment'

urlpatterns = [
    url(r'^appt/',views.book_patient,name="book"),


]

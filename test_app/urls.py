from django.conf.urls import url
from test_app import views

app_name='test_app'

urlpatterns = [

    # url(r'^register/$',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^lab_login/',views.lab_login,name='lab_login'),
    # url(r'^doctor_pt/$',views.doctor_pt,name='doctor_portal'),
    # url(r'^appointments_d/',views.appointment_d,name='appointment_d'),
]

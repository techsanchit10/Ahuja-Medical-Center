from django.conf.urls import url
from doctors_app import views

app_name='doctors_app'

urlpatterns = [

    # url(r'^register/$',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^d_login/',views.d_login,name='doctor_login'),
    url(r'^doctor_pt/$',views.doctor_pt,name='doctor_portal'),
    url(r'^appointments_d/',views.appointment_d,name='appointment_d'),
    url(r'^log_out/',views.user_logout,name='logout'),
    # url(r'^admin/', admin.site.urls),

]

from django.conf.urls import url
from basic_app import views


app_name='basic_app'

urlpatterns = [

    url(r'^registration/$',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^surgeon/$',views.spcl_surgeon,name='surgeon'),
    url(r'^ent/$',views.spcl_ent,name='ent'),
    url(r'^gynaecologist/$',views.spcl_gynae,name='gynae'),
    url(r'^gen-phy/$',views.spcl_gen_phy,name='gen_phy'),
    url(r'^my-prsc/$',views.prsc,name='prescriptions'),
    url(r'^my-appt/$',views.appointment,name='appointment'),
    # url(r'^my-prsc/(?P<pk>[-\w]+)/$',views.PrescriptionDetailView.as_view()),
    url(r'^search/$',views.search,name='search'),
    # url(r'^profile/$',views.pro1,name='profile'),



]

from django.conf.urls import url
from epr_app import views

app_name='epr_app'

urlpatterns = [
    url(r'^epr/',views.epr_register,name="epr"),
    url(r'^exist-epr/',views.exist_epr_register,name = "exist"),
]

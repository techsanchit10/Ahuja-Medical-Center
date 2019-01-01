from django.contrib import admin

from epr_app.models import mst_user
from epr_app.models import mst_patient
from epr_app.models import mst_test
from epr_app.models import mst_doctor
from epr_app.models import mst_specialization
from epr_app.models import appt_doctor
from epr_app.models import doct_specializ
from epr_app.models import mst_payment
from epr_app.models import transaction_appt
from epr_app.models import exist_patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('p_id','p_fname','p_lname','d_name')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('app_no','d_name')

class ExistPatientAdmin(admin.ModelAdmin):
    list_display = ('p_id','d_name')

admin.site.register(mst_user)
admin.site.register(mst_patient,PatientAdmin)
admin.site.register(mst_test)
admin.site.register(mst_doctor)
admin.site.register(mst_specialization)
admin.site.register(doct_specializ)
admin.site.register(appt_doctor,AppointmentAdmin)
admin.site.register(mst_payment)
admin.site.register(transaction_appt)
admin.site.register(exist_patient,ExistPatientAdmin)
# Register your models here.

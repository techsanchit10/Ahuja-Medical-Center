from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo2(models.Model):

    #Create relationship
    user=models.OneToOneField(User)

    doctors_appt = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.doctors_appt
# # Create your models here.
# from django.db import models
# from datetime import date
#
# # Create your models here.
# class mst_user(models.Model):
#     username=models.CharField(max_length=264,unique=True)
#     u_fname=models.CharField(max_length=264)
#     u_lname=models.CharField(max_length=264)
#     email=models.EmailField(max_length=264)
#     phone=models.PositiveIntegerField(max_length=264)
#     address=models.CharField(max_length=264)
#     pincode=models.PositiveIntegerField(max_length=6)
#     gender_choices=(
#                     ('M','Male'),
#                     ('F','Female'),
#                     ('O','Other'),)
#     gender=models.CharField(max_length=1,choices=gender_choices)
#     date_of_birth=models.DateField()
#     # password=models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.username
#
# class mst_specialization(models.Model):
#     sp_id=models.CharField(max_length=264,unique=True)
#     sp_name=models.CharField(max_length=264)
#     #d_id=models.ForeignKey(doctor)
#     d_name=models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.sp_id
#
# class mst_doctor(models.Model):
#     d_id=models.CharField(max_length=264,unique=True,)
#     d_fname=models.CharField(max_length=264)
#     d_lname=models.CharField(max_length=264)
#     email=models.EmailField(max_length=264)
#     phone=models.PositiveIntegerField(max_length=264)
#     specializ=models.CharField(max_length=264)
#     sp_id=models.ForeignKey(mst_specialization)
#     cons_pers_fee=models.PositiveIntegerField(max_length=264)
#     cons_online_fee=models.PositiveIntegerField(max_length=264)
#
#     def __str__(self):
#         return self.d_id
#
# class doct_specializ(models.Model):
#     d_id=models.ForeignKey(mst_doctor)
#     so_id=models.ForeignKey(mst_specialization)
#
#
# class mst_patient(models.Model):
#     p_id=models.CharField(max_length=264,unique=True)
#     username=models.ForeignKey(mst_user)
#     p_fname=models.CharField(max_length=264)
#     p_lname=models.CharField(max_length=264)
#     email=models.EmailField(max_length=264)
#     phone=models.PositiveIntegerField(max_length=264)
#     address=models.CharField(max_length=264)
#     pincode=models.PositiveIntegerField(max_length=264)
#     gender_choices=(
#                     ('M','Male'),
#                     ('F','Female'),)
#     gender=models.CharField(max_length=1,choices=gender_choices)
#     date_of_birth=models.DateField()
#     d_id=models.ForeignKey(mst_doctor)
#     d_name=models.CharField(max_length=264)
#     #sp_id=models.ForeignKey(specialization)
#     specialization=models.CharField(max_length=264)
#     prob_des=models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.p_id
#
# class mst_test(models.Model):
#     t_id=models.CharField(max_length=264,unique=True)
#     t_name=models.CharField(max_length=264)
#     d_id=models.CharField(max_length=264)
#     d_name=models.CharField(max_length=264)
#     specialization=models.CharField(max_length=264)
#     p_id=models.ForeignKey(mst_patient)
#     username=models.CharField(max_length=264)
#
# class appt_doctor(models.Model):
#     p_id=models.ForeignKey(mst_patient)
#     app_no=models.PositiveIntegerField(max_length=264,unique=True)
#     p_fname=models.CharField(max_length=264)
#     p_lname=models.CharField(max_length=264)
#     email=models.EmailField(max_length=264)
#     phone=models.PositiveIntegerField(max_length=264)
#     address=models.CharField(max_length=264)
#     pincode=models.PositiveIntegerField(max_length=264)
#     date_of_birth=models.DateField()
#     d_id=models.ForeignKey(mst_doctor)
#     d_name=models.CharField(max_length=264)
#     specialization=models.CharField(max_length=264)
#
# class mst_payment(models.Model):
#     pm_id=models.CharField(max_length=264,unique=True)
#     username=models.ForeignKey(mst_user)
#     trans_date=models.DateField(("Date"),default=date.today)
#     trans_time=models.TimeField(("Time"),blank=True)
#     pm_mode=models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.pm_id
#
# class transaction_appt(models.Model):
#     p_id=models.ForeignKey(mst_patient)
#     appt_no=models.CharField(max_length=264,unique=True)
#     pm_id=models.ForeignKey(mst_payment)
#     appt_date=models.DateField(("Date"),default=date.today)
#     appt_time=models.TimeField(("Time"),blank=True)
#     d_id=models.ForeignKey(mst_doctor)
#     d_name=models.CharField(max_length=264)

from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class mst_user(models.Model):
    # username=models.CharField(max_length=264,unique=True)
    # u_fname=models.CharField(max_length=264)
    # u_lname=models.CharField(max_length=264)
    # email=models.EmailField(max_length=264)

    user = models.OneToOneField(User)

    phone=models.PositiveIntegerField()
    address=models.CharField(max_length=264)
    pincode=models.PositiveIntegerField()
    gender_choices=(
                    ('M','Male'),
                    ('F','Female'),
                    ('O','Other'),)
    gender=models.CharField(max_length=1)
    date_of_birth=models.DateField()


    def __str__(self):
        return self.user.username

class mst_specialization(models.Model):
    # sp_id=models.CharField(max_length=264,unique=True)
    sp_name=models.CharField(max_length=264,unique=True)
    #d_id=models.ForeignKey(doctor)
    d_name=models.CharField(max_length=264)

    def __str__(self):
        return self.sp_name

class mst_doctor(models.Model):
    user = models.OneToOneField(User)

    d_id1=models.CharField(max_length=264,unique=True)
    d_fname=models.CharField(max_length=264)
    d_lname=models.CharField(max_length=264)
    # email=models.EmailField(max_length=264)
    phone=models.PositiveIntegerField()
    sp_name=models.ForeignKey(mst_specialization)
    # sp_id=models.ForeignKey(mst_specialization)
    cons_pers_fee=models.PositiveIntegerField()
    cons_online_fee=models.PositiveIntegerField()
    dr_appt_date=models.DateField(max_length=264)

    def __str__(self):
        return self.d_id1

class doct_specializ(models.Model):
    d_id1=models.ForeignKey(mst_doctor)
    sp_name=models.ForeignKey(mst_specialization)



class mst_patient(models.Model):
    user_id = models.ForeignKey(User)

    p_id=models.CharField(max_length=100,unique=True,blank=True)
    p_fname=models.CharField(max_length=264)
    p_lname=models.CharField(max_length=264)
    email=models.EmailField(max_length=264)
    phone=models.PositiveIntegerField()
    address=models.CharField(max_length=264)
    pincode=models.PositiveIntegerField()

    gender=models.CharField(max_length=10)
    date_of_birth=models.CharField(max_length=50)
    # sp_name=models.ForeignKey(mst_specialization)

    # d_id1=models.ForeignKey(mst_doctor)
    d_name=models.CharField(max_length=264,blank = True)
    #sp_id=models.ForeignKey(specialization)
    prob_des=models.TextField(max_length=1000)
    pres = models.TextField(max_length=1000,blank = True)


    def __str__(self):
        # return self.id
        # return self.p_fname
        # return self.p_id
        return ("P_" + self.p_id + " : " + self.p_fname)

class exist_patient(models.Model):
    p_id = models.ForeignKey(mst_patient)
    d_name = models.CharField(max_length=300)

    # user= models.ForeignKey(User)
    prob_des=models.TextField(max_length=1000)
    pres = models.TextField(max_length=1000,blank = True)

class appt_doctor(models.Model):
    user = models.ForeignKey(User,blank=True,null=True)

    p_id=models.ForeignKey(mst_patient)
    app_no=models.CharField(max_length=50,unique=True,blank=True)
    # p_fname=models.CharField(max_length=264)
    # p_lname=models.CharField(max_length=264)
    # email=models.EmailField(max_length=264)
    phone=models.PositiveIntegerField(blank=True,null=True)
    address=models.CharField(max_length=264)
    pincode=models.PositiveIntegerField(null=True)
    date_of_birth=models.CharField(max_length=50,null=True)
    
    # sp_name=models.ForeignKey(mst_specialization,blank=True)
    # d_id1=models.ForeignKey(mst_doctor)
    d_name=models.CharField(max_length=264)
    appt_date=models.DateField(("Date"),default=date.today)




class mst_test(models.Model):
    user = models.OneToOneField(User)

    t_id=models.CharField(max_length=264,unique=True)
    t_name=models.CharField(max_length=264)
    d_id1=models.CharField(max_length=264)
    d_name=models.CharField(max_length=264)
    sp_name=models.ForeignKey(mst_specialization)
    p_id=models.ForeignKey(mst_patient)
    # username=models.CharField(max_length=264)




class mst_payment(models.Model):
    user = models.OneToOneField(User)

    pm_id=models.CharField(max_length=264,unique=True)
    # username=models.ForeignKey(mst_user)
    trans_date=models.DateField(("Date"),default=date.today)
    trans_time=models.TimeField(("Time"),blank=True)
    pm_mode=models.CharField(max_length=264)

    def __str__(self):
        return self.pm_id

class transaction_appt(models.Model):
    p_id=models.ForeignKey(mst_patient)
    appt_no=models.CharField(max_length=264,unique=True)
    pm_id=models.ForeignKey(mst_payment)
    appt_date=models.DateField(("Date"),default=date.today)
    appt_time=models.TimeField(("Time"),blank=True)
    d_id1=models.ForeignKey(mst_doctor)
    d_name=models.CharField(max_length=264)

    def __str__(self):
        return self.p_id

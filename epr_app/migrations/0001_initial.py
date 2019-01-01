# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-17 16:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appt_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_no', models.CharField(blank=True, max_length=50, unique=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=264)),
                ('pincode', models.PositiveIntegerField(null=True)),
                ('date_of_birth', models.CharField(max_length=50, null=True)),
                ('sp_name', models.CharField(max_length=50)),
                ('d_name', models.CharField(max_length=264)),
                ('appt_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='doct_specializ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='exist_patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=300)),
                ('prob_des', models.TextField(max_length=1000)),
                ('pres', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='mst_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id1', models.CharField(max_length=264, unique=True)),
                ('d_fname', models.CharField(max_length=264)),
                ('d_lname', models.CharField(max_length=264)),
                ('phone', models.PositiveIntegerField()),
                ('cons_pers_fee', models.PositiveIntegerField()),
                ('cons_online_fee', models.PositiveIntegerField()),
                ('dr_appt_date', models.DateField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='mst_patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(blank=True, max_length=100, unique=True)),
                ('p_fname', models.CharField(max_length=264)),
                ('p_lname', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264)),
                ('phone', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=264)),
                ('pincode', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('sp_name', models.CharField(max_length=50)),
                ('d_name', models.CharField(blank=True, max_length=264)),
                ('prob_des', models.TextField(max_length=1000)),
                ('pres', models.TextField(blank=True, max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mst_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_id', models.CharField(max_length=264, unique=True)),
                ('trans_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('trans_time', models.TimeField(blank=True, verbose_name='Time')),
                ('pm_mode', models.CharField(max_length=264)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mst_specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=264, unique=True)),
                ('d_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='mst_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.CharField(max_length=264, unique=True)),
                ('t_name', models.CharField(max_length=264)),
                ('d_id1', models.CharField(max_length=264)),
                ('d_name', models.CharField(max_length=264)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_patient')),
                ('sp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mst_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=264)),
                ('pincode', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transaction_appt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appt_no', models.CharField(max_length=264, unique=True)),
                ('appt_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('appt_time', models.TimeField(blank=True, verbose_name='Time')),
                ('d_name', models.CharField(max_length=264)),
                ('d_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_doctor')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_patient')),
                ('pm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_payment')),
            ],
        ),
        migrations.AddField(
            model_name='mst_doctor',
            name='sp_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_specialization'),
        ),
        migrations.AddField(
            model_name='mst_doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exist_patient',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_patient'),
        ),
        migrations.AddField(
            model_name='doct_specializ',
            name='d_id1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_doctor'),
        ),
        migrations.AddField(
            model_name='doct_specializ',
            name='sp_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_specialization'),
        ),
        migrations.AddField(
            model_name='appt_doctor',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epr_app.mst_patient'),
        ),
        migrations.AddField(
            model_name='appt_doctor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
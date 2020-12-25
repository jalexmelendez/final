from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='user_id')
    date_created = models.CharField(max_length=225)
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    is_supervisor = models.BooleanField(default=False)
    super_watchlist = models.CharField(max_length=225)
    super_groups_id = models.CharField(max_length=225)
    super_school = models.CharField(max_length=225)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    age = models.CharField(max_length=225)
    profile_pic = models.CharField(max_length=225)
    mail = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    current_lesson = models.CharField(max_length=225)
    difficulty_load = models.CharField(max_length=225)
    score = models.IntegerField(default=0)
    avg_1 = models.CharField(max_length=225)
    avg_2 = models.CharField(max_length=225)
    avg_3 = models.CharField(max_length=225)
    avg_4 = models.CharField(max_length=225)

class achieve(models.Model):
    username = models.CharField(max_length=225)
    a1 = models.CharField(max_length=225)
    a2 = models.CharField(max_length=225)
    a3 = models.CharField(max_length=225)
    a4 = models.CharField(max_length=225)
    a5 = models.CharField(max_length=225)
    a6 = models.CharField(max_length=225)
    a7 = models.CharField(max_length=225)
    a8 = models.CharField(max_length=225)
    a9 = models.CharField(max_length=225)
    a10 = models.CharField(max_length=225)

class test(models.Model):
    username = models.CharField(max_length=225)
    q1 = models.CharField(max_length=225)
    q2 = models.CharField(max_length=225)
    q3 = models.CharField(max_length=225)
    q4 = models.CharField(max_length=225)
    q5 = models.CharField(max_length=225)
    q6 = models.CharField(max_length=225)
    q7 = models.CharField(max_length=225)
    q8 = models.CharField(max_length=225)
    q9 = models.CharField(max_length=225)
    q10 = models.CharField(max_length=225)
    q11 = models.CharField(max_length=225)
    q12 = models.CharField(max_length=225)
    q13 = models.CharField(max_length=225)
    q14 = models.CharField(max_length=225)
    q15 = models.CharField(max_length=225)
    q16 = models.CharField(max_length=225)
    q17 = models.CharField(max_length=225)
    q18 = models.CharField(max_length=225)
    q19 = models.CharField(max_length=225)
    q20 = models.CharField(max_length=225)
    q21 = models.CharField(max_length=225)
    q22 = models.CharField(max_length=225)
    q23 = models.CharField(max_length=225)
    q24 = models.CharField(max_length=225)
    q25 = models.CharField(max_length=225)

class school(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='s_id')
    date_created = models.CharField(max_length=225)
    total_score = models.CharField(max_length=225)
    avg_score = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    responsable = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    users_id_in_school = models.CharField(max_length=225)
    groups_id_in_school = models.CharField(max_length=225)
    optional_password = models.CharField(max_length=225)

class school_group(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='group_id')
    group_supervisor = models.CharField(max_length=225)
    users_id_array = models.CharField(max_length=225)
    school = models.CharField(max_length=225)
    group_avg = models.CharField(max_length=225)


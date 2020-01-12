import datetime

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models

from .constant import *
from .validators import *


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    first_name = models.CharField(max_length=255, validators=[CharFieldValidator(), ])
    last_name = models.CharField(max_length=255, blank=True, null=True, validators=[CharFieldValidator(), ])
    dob = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    username = models.CharField(max_length=255, unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER, max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=20, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    country = models.CharField(max_length=255)
    study_grd = models.CharField(max_length=50)
    study_board = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone', 'dob', 'gender', 'country']

    objects = UserManager()

    def __str__(self):
        return self.username


class Class(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    question = models.TextField()


class UserClass(models.Model):
    user_id = models.ForeignKey(get_user_model(), related_name='student', on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)


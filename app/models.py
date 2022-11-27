from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import *

class CustomUser(AbstractUser):
    GENDER={
        ('m','male'),
        ('f','female'),
        ('o','other'),
    }
    username = None
    frist_name=models.CharField(max_length=255, null=True,blank=True)
    last_name=models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender= models.CharField(max_length=255, choices=GENDER,default='None')
    age=models.DateTimeField(auto_now=False, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['frist_name','last_name','phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
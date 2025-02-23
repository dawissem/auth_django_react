from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class CustemUserManager(BaseUserManager):
   def create_user():
       pass
   def create_suepruser():
       pass

class customeUser(AbstractUser):
    email = models.EmailField(max_length=200,unique=True)
    birthday =models.DateField(null=True, blank=True)
    USERNAME_FIELD='email'     
    REQUIRED_FIELDS= []
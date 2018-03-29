from django.db import models

# Create your models here.
from django.cotrib.auth.models import AbstracUser,UserManager 

class CustomUserManager(UserManager):
	pass

class CustomUser(AbstrsctUser):
	objects = CustomUserManager()
		


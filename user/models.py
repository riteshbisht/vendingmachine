from django.db import models
from django.contrib.auth.models import AbstractUser
from util.models import AbstractAutoDate

# Create your models here.
class User(AbstractUser):
    pass

class BuyUser(AbstractAutoDate):
    mobile_number = models.CharField(max_length=15)


    def __str__(self):
    	return self.mobile_number
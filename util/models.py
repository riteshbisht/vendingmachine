from django.db import models

# Create your models here.
class AbstractAutoDate(models.Model):
	class Meta:
		abstract = True
	create_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)
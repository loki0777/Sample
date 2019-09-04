from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db import *



class meUser(models.Model):
	name = models.CharField(max_length=50, blank=False, null=True)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=20)
	DD = models.IntegerField()
	MM = models.IntegerField()
	YYYY = models.IntegerField()

	def saveUser(self):
		self.save()

	def __str__(self):
		return self.name

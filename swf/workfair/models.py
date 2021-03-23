from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

class ApplicantProfile(models.Model):
	name = models.CharField(max_length = 50)
	dob = models.DateField()
	email = models.EmailField()
	description = models.TextField()
	username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class EmployerProfile(models.Model):
	name = models.CharField(max_length = 64)
	description = models.TextField()
	username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Vacancy(models.Model):
	name = models.CharField(max_length = 64)
	competences = models.CharField(max_length = 32)
	salary = models.DecimalField(decimal_places = 2, max_digits = 10)
	description = models.TextField(null = True)
	company = models.ForeignKey(EmployerProfile, on_delete = models.CASCADE)
	featured = models.BooleanField(default = False)
	viewsAmount = models.IntegerField(default = 0)
	creationDate = models.DateTimeField(auto_now = True)
	phoneNumber = models.IntegerField(default = 89990870968)

	def getAbsoluteUrl(self):
		return f"/vacancy/{self.id}/"

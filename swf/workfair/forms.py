from django import forms

from .models import Vacancy, ApplicantProfile, EmployerProfile

class VacancyAddForm(forms.ModelForm):
	class Meta:
		model = Vacancy
		fields = [
			'name',
			'competences',
			'description',
			'salary',
		]
class ApplicantProfileEdit(forms.ModelForm):
	class Meta:
		model = ApplicantProfile
		fields = [
			'name',
			'dob',
			'email',
			'description',
		]
class EmployerProfileEdit(forms.ModelForm):
	class Meta:
		model = EmployerProfile
		fields = [
			'name',
			'description',
		]
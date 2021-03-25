from django import forms

from .models import Vacancy, ApplicantProfile, EmployerProfile

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class VacancyAddForm(forms.ModelForm):
	class Meta:
		model = Vacancy
		fields = [
			'name',
			'competences',
			'description',
			'salary',
			'phoneNumber',
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
class sortChoice(forms.Form):
	CHOICES = [('creationDate', 'Сортировать по дате'),
				('viewsAmount', 'Сортировать по популярности'),]
	choice = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect, label = 'Сортировка по', required = False)
	
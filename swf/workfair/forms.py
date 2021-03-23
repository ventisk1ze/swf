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

# class CustomAuntethicationForm(AuthenticationForm):
# 	username = UsernameField(
# 		label = 'Логин',
# 		widget = forms.TextInput(attrs={'autofocus': True})
# 	)
# 	password = PasswordField(
# 		label = 'Пароль',
# 		widget = forms.TextInput(attrs={'autofocus': True})
# 	)
	
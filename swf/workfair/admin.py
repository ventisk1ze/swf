from django.contrib import admin

from .models import ApplicantProfile, EmployerProfile, Vacancy
admin.site.register(ApplicantProfile)
admin.site.register(EmployerProfile)
admin.site.register(Vacancy)
# Register your models here.

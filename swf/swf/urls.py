from django.contrib import admin

from django.urls import path

from workfair import views

urlpatterns = [
	path('', views.homeView, name = 'home'),

    path('addvacancy/', views.vacancyAddView, name = 'addvacancy'),

	path('login/', views.loginView, name = 'login'),

	path('register_applicant/', views.ApplRegisterView, name = 'registerappl'),

    path('register_HR/', views.EmplRegisterView, name = 'registerhr'),

    path('logout/', views.logoutView, name='logout'),

    path('admin/', admin.site.urls),

    path('profile/', views.profileView, name = 'profile'),

    path('profilesetup/', views.profileSetupView, name='ProfileSetup'),

    path('profileupdate/', views.profileUpdateView, name='ProfileUpdate'),

    path('vacancy/<int:id>/', views.dynamicVacancyView, name = 'vacancy'),

    path('allvacancies', views.vacancyListView, name = 'vacancyList'),
]


from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, Http404

from .forms import VacancyAddForm, ApplicantProfileEdit, EmployerProfileEdit

from .models import ApplicantProfile, EmployerProfile, Vacancy

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout

from django.contrib.auth.models import Group, User

from django.contrib.auth.decorators import login_required

from django.db.models import Q

def EmplRegisterView(request):
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name = 'Employers')
			user.groups.add(group)
			login(request, user)
			return redirect('ProfileSetup')
	else:
		if request.user.is_authenticated:
			logout(request)
		form = UserCreationForm()
	context = {
		'form':form,
	}
	
	return render(request, "registerPage.html", context)

def ApplRegisterView(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name = 'Job seekers')
			user.groups.add(group)
			login(request, user)
			return redirect('ProfileSetup')
	else:
		if request.user.is_authenticated:
			logout(request)
		form = UserCreationForm()
	context = {
		'form':form,
	}
	
	return render(request, "regappl.html", context)

def loginView(request):
	
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('profile')
	else:
		form = AuthenticationForm()
	context = {
		'form':form,
	}
	return render(request, 'loginPage.html', context)

def logoutView(request):
	if request.method == 'POST':
		logout(request)
	return redirect('home')

@login_required(login_url = 'login')
def vacancyAddView(request):
	if request.method == 'POST':
		form = VacancyAddForm(request.POST)
		if form.is_valid():
			form.instance.company = request.user.employerprofile
			form.save()
			return redirect('profile')
	else:
		form = VacancyAddForm()
	context = {
		'form':form
	}

	return render(request, "addVacancy.html", context)

@login_required(login_url = 'login')
def profileView(request):
	if request.user.groups.filter(name = 'Job seekers'):
		obj = ApplicantProfile.objects.get(username = request.user)
		return render(request, "applicantProfile.html", {'obj' : obj})
	else:
		obj = EmployerProfile.objects.get(username = request.user)
		return render(request, "employerProfile.html", {'obj' : obj})

@login_required(login_url = 'login')
def profileSetupView(request):
	if request.user.groups.filter(name = 'Job seekers'):
		if request.method == 'POST':
			form = ApplicantProfileEdit(request.POST)
			if form.is_valid():
				form.instance.username = request.user
				form.save()
				return redirect('profile')
		else:
			form = ApplicantProfileEdit()

	else:
		if request.method == 'POST':
			form = EmployerProfileEdit(request.POST)
			if form.is_valid():
				form.instance.username = request.user
				form.save()
				return redirect('profile')
		else:
			form = EmployerProfileEdit()
	context = {
		'form':form
	}		
	return render(request, "ProfileSetup.html", context)

@login_required(login_url = 'login')
def profileUpdateView(request):
	if request.user.groups.filter(name = 'Job seekers'):
		thisInstance = ApplicantProfile.objects.get(username = request.user)
		if request.method == 'POST':
			form = ApplicantProfileEdit(request.POST, instance = thisInstance)
			if form.is_valid():
				form.save()
				return redirect('profile')
		else:
			form = ApplicantProfileEdit(instance = thisInstance)
	else:
		thisInstance = EmployerProfile.objects.get(username = request.user)
		if request.method == 'POST':
			form = EmployerProfileEdit(request.POST, instance = thisInstance)
			if form.is_valid():
				form.save()
				return redirect('profile')
		else:
			form = EmployerProfileEdit(instance = thisInstance)
	context = {
		'form':form
	}
	return render(request, "ProfileUpdate.html", context)

def homeView(request):
	return render(request, "home.html", {})

@login_required(login_url = 'login')
def dynamicVacancyView(request, id):
	obj = get_object_or_404(Vacancy, id = id)
	obj.viewsAmount += 1
	obj.save()
	context = {
		'obj' : obj
	}
	return render(request, "vacancy.html", context)

@login_required(login_url = 'login')
def vacancyListView(request):
	searchQueryNavbar = request.GET.get('search_navbar', '')
	searchQueryVLpage = request.GET.get('search_vlpage', '')

	if searchQueryNavbar or searchQueryVLpage:
		if searchQueryNavbar:
			searchQuery = searchQueryNavbar
		else:
			searchQuery = searchQueryVLpage
		queryset = Vacancy.objects.filter(Q(name__icontains = searchQuery) | Q(salary__icontains = searchQuery) | Q(competences__icontains = searchQuery)).order_by('-viewsAmount')
	else:
		queryset = Vacancy.objects.all()

	context = {
		'objectList':queryset
	}
	return render(request, "vacancyList.html", context)

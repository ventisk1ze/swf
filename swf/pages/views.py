from django.shortcuts import render
from django.http import HttpResponse
def homeView(request, *args, **kwargs):
	return render(request, "home.html", {})
	
def loginPageView(request, *args, **kwargs):
	myContext = {
		"huysgovnom" : 123,
		"dimaTroshin" : "pidaras",
	}
	return render(request, "loginPage.html",myContext)

def registerPageView(request, *args, **kwargs):
	return render(request, "registerPage.html",{})

def profileView(request, *args, **kwargs):
	return render(request, "profile.html",{})

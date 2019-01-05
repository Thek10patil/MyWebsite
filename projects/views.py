from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects, Courses, Aboutme, Contacts

# Create your views here.
def projects(request):
	# return HttpResponse("<h1>ketan</h1>").

	projects = Projects.objects.all()

	context ={
		'title':'Projects',
		'projects':projects
	}

	return render(request, 'projects/index.html', context)


def details(request, id):
	project = Projects.objects.get(id=id)

	context = {
		'project':project
	}

	return render(request, "projects/details.html", context)

def courses(request):
	courses = Courses.objects.all()

	context ={
		'courses':courses
	}
	return render(request, "projects/courses.html", context)

def aboutme(request):
	about = Aboutme.objects.all()
	context = {
		'about':about
	}
	return render(request, "projects/aboutme.html", context)

def contact(request):
	contacts = Contacts.objects.all()
	context = {
		'contact':contacts
	}
	return render(request, "projects/contact.html", context)
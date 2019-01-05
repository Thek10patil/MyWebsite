from django.contrib import admin

# Register your models here.
from .models import Projects, Courses, Aboutme, Contacts

admin.site.register(Projects)
admin.site.register(Courses)
admin.site.register(Aboutme)
admin.site.register(Contacts)
	
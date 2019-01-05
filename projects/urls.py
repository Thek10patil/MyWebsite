from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.aboutme, name = 'aboutme'),
    url(r'^details/(?P<id>\d+)/$', views.details, name = 'details'),
    path('courses/', views.courses, name = 'courses'),
    path('aboutme/', views.aboutme, name = 'aboutme'),
    path('contact/', views.contact, name = 'contact'),
    path('projects/', views.projects, name = 'projects'),   
]


urlpatterns += staticfiles_urlpatterns()
# projects/urls.py

from django.contrib import admin
from django.urls import path,include
from projects import views

# Django Admin header customization
admin.site.site_header = "Harshith"
admin.site.site_title = "Welcome to Harshith"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("projects", views.projects, name="projects"),
    path("certificates", views.certificates, name="certificates"),
    path("resume", views.resume, name="resume"),
]

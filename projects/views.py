# projects/views.py

# projects/views.py

from django.shortcuts import render, HttpResponse
from .models import Project, Certification, Contact

# Homepage view with sections
def home(request):
    return render(request, 'home.html')

# Projects view
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

# Certificates view
def certificates(request):
    certificates = Certification.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})
def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        desc = request.POST["desc"]
        # print(name, email, desc)
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()

    return render(request, "contact.html")
# Resume view
def resume(request):
      # Assuming there is only one resume
    return render(request, "resume.html")


# Create your views here.

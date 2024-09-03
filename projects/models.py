from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
class Certification(models.Model):
    name=models.CharField(max_length=50)
    issuer=models.CharField(max_length=50)
    date_earned=models.DateField
    image=models.ImageField(upload_to='certificate_images/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.name
'''  
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f'Resume {self.id}'
'''
# Create your models here.

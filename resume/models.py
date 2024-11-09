from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField()
    skills = models.TextField()  # comma-separated for simplicity
    experience = models.TextField()  # JSON-style or raw text for simplicity
    education = models.TextField()  # JSON-style or raw text

    def __str__(self):
        return self.name

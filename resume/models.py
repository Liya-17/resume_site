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

from django.db import models

class ContactMessage(models.Model):
    """Model for storing contact form messages."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class Project(models.Model):
    """Model for showcasing projects in the portfolio."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional link to the project (e.g., GitHub)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

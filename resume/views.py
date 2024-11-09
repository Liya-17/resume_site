from django.shortcuts import render

# Create your views here.
from .models import Resume
from .forms import ContactForm


def resume_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can process the form data here (send an email, save to database, etc.)
            # For now, we just print the data to the console.
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Message: {form.cleaned_data['message']}")
    else:
        form = ContactForm()

    return render(request, 'resume/resume.html', {'form': form})

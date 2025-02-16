from django.shortcuts import render,redirect
from django.contrib import messages
from .models import contact,about_me,skill,project

# Create your views here.
def home_view(request):
    skills = skill.objects.all()
    projects = project.objects.all()
    about = about_me.objects.all()
    context ={
        'about':about,
        'skills':skills,
        'projects':projects,
    }
    return render(request, 'index.html',context)
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            messages.success(request, "Your message has been sent!")
            contact.objects.create(name=name,email=email,message=message)
            return redirect('/')
        else:
            messages.error(request, "Please fill out all fields!")
            return redirect('/')
    return redirect('/')

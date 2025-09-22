from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def projects(request):
    return render(request, 'home/projects.html')

def blog(request):
    return render(request, 'home/blog.html')

def resume(request):
    return render(request, 'home/resume.html')

def contact(request):
    return render(request, 'home/contact.html')

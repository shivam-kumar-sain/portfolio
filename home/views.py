from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Project,Blog
import os
from .forms import ProjectForm,BlogForm
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    projects = Project.objects.all().order_by("-created_at")[:3]
    blogs= Blog.objects.all().order_by("-created_at")[:3]
    return render(request, 'home/index.html',{'projects':projects,'blogs':blogs})


def projects(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            if project.project_img:
                ext = project.project_img.name.split('.')[-1]
                new_name = f"projects/{project.id}.{ext}"
                if project.project_img.name != new_name:
                    old_path = project.project_img.path
                    project.project_img.name = new_name
                    project.save()
                    if os.path.exists(old_path) and old_path != project.project_img.path:
                        os.remove(old_path)
            return redirect("projects")
    else:
        form = ProjectForm()
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "home/projects.html", {"projects": projects, "form": form})

def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            if 'project_img' in request.FILES:
                if project.project_img and os.path.exists(project.project_img.path):
                    os.remove(project.project_img.path)
                project.project_img = request.FILES['project_img']
            project.save()
            if project.project_img:
                ext = project.project_img.name.split('.')[-1]
                project.project_img.name = f"projects/{project.id}.{ext}"
                project.save()
            if request.headers.get("HX-Request"):
                return HttpResponse(
                    "<script>document.getElementById('modalEdit').close(); window.location.reload();</script>"
                )
    else:
        form = ProjectForm(instance=project)

    return render(request, "home/partials/update_form.html", {"form": form, "project": project})

def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            if blog.image:
                ext = blog.image.name.split('.')[-1] 
                new_name = f"blog/{blog.id}.{ext}"
                new_path = os.path.join(settings.MEDIA_ROOT, new_name)

                old_path = blog.image.path
                os.rename(old_path, new_path)
                blog.image.name = new_name
                blog.save()
            return redirect("blog")
    else:
        form = BlogForm()

    blogs = Blog.objects.all().order_by("-created_at")[:6]
    return render(request, "home/blog.html", {"blogs": blogs, "form": form})

def update_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            if 'image' in request.FILES and blog.image:
                if os.path.exists(blog.image.path):
                    os.remove(blog.image.path)
            blog.save()
            if request.headers.get("HX-Request"):
                return HttpResponse(
                    "<script>document.getElementById('modalEdit').close(); window.location.reload();</script>"
                )
    else:
        form = BlogForm(instance=blog)

    return render(request, "home/partials/blog_detail_partial.html", {"form": form, "blog": blog})

def resume(request):
    return render(request, 'home/resume.html')

def contact(request):
    return render(request, 'home/contact.html')

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_html_email(request):
    try:
        subject = "Welcome to MySite"
        to_email = "shivamkumar6399029@gmail.com"
        html_content = render_to_string(
            "emails/welcome.html",
            {"username": "Shivam"} 
        )
        email = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        return HttpResponse("HTML Email sent successfully!")
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def clientMail(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject_text = request.POST.get("subject")
            message_text = request.POST.get("message")

            subject = f"New Contact Message: {subject_text}"
            to_email = "shivamkumar6399029@gmail.com"

            html_content = render_to_string(
                "emails/inqury.html",
                {"name": name, "email": email, "subject": subject_text, "message": message_text}
            )
            email_msg = EmailMessage(
                subject=subject,
                body=html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[to_email],
            )
            email_msg.content_subtype = "html"
            email_msg.send(fail_silently=False)
            if request.headers.get("HX-Request"):
                return HttpResponse("<p>✅ Your message has been sent successfully!</p>")

            return HttpResponse("HTML Email sent successfully!")

        return HttpResponse("Invalid request method.")

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")


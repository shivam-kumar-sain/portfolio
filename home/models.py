from django.db import models
import os

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Custom User Manager
class UserTableManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, fullname, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, fullname, password, **extra_fields)
# 1. User Table (Custom Auth)
class UserTable(AbstractUser):
    username = None
    fullname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    objects = UserTableManager()

    class Meta:
        db_table = "user_table"

    def __str__(self):
        return self.fullname


# 2. User Details
class UserDetails(models.Model):
    user = models.OneToOneField(UserTable, on_delete=models.CASCADE, related_name="details")
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    designation = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = "user_details" 

    def __str__(self):
        return f"{self.user.fullname} - {self.designation}"


# 3. Bloge
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bloge"

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "inqurai"

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"
    
def project_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('projects/', filename)
class Project(models.Model):
    STATUS_CHOICES = [
        ('live', 'Live'),
        ('working', 'Working'),
        ('holding', 'Holding'),
    ]
    project_name = models.CharField(max_length=200)
    project_img = models.ImageField(upload_to=project_image_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='working')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.project_name

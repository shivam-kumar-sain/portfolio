from django.contrib.auth.models import AbstractUser


# 1. User Table (Custom Auth)
class UserTable(AbstractUser):
    username = None  # we don't need username
    fullname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    class Meta:
        db_table = "user_table"   # ✅ custom table name

    def __str__(self):
        return self.fullname


# 2. User Details
class UserDetails(models.Model):
    user = models.OneToOneField(UserTable, on_delete=models.CASCADE, related_name="details")
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    designation = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = "user_details"   # ✅ custom table name

    def __str__(self):
        return f"{self.user.fullname} - {self.designation}"


# 3. Bloge
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bloge"   # ✅ custom table name

    def __str__(self):
        return self.title


# 4. Inqurai
class Inquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "inqurai"   # ✅ custom table name

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"

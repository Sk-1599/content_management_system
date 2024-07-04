
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6)
    is_admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=True)

class ContentItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/')
    categories = models.ManyToManyField("Category")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')

class Category(models.Model):
    name = models.CharField( max_length=50)
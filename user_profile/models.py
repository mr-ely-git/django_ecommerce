from django.db import models
from django.contrib.auth.models import User


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True, unique=True)
    email_activation_code = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


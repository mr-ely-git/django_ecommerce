from django.db import models


# Create your models here.

class ContactUsMessage(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False)




from django.db import models

class Contact(models.Model):
    """model class for contact form"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

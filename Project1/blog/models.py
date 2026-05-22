from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class User(models.Model):
#     fname = models.CharField(max_length=75, help_text="First name")
#     lname = models.CharField(max_length=75, help_text="Last name")
#     email = models.EmailField(help_text="Email")
#     password = models.ForeignKey(max_length=255, help_text="New password")

# py -m venv venv
# .\venv\Scripts\activate
# pip install django
# django-admin startproject MyApp
# cd MyApp
# py manage.py startapp blog 
# py manage.py runserver
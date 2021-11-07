from typing import Text
from django.db import models
from django.db.models.fields import TextField


career = (
    ('Accounts', 'Accounts'),
    ('Administration', 'Administration'),
    ('Human Resources', 'Human Resources'),
    ('Technical', 'Technical'),
    ('Sales', 'Sales')
)


def upload_review_photo(instance, filename, *kwargs):
    file_path ='{filename}'.format(filename=filename)
    return file_path


# Create your models here.
class CareerRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    interest = models.CharField(max_length=255, choices=career, default=None)
    position = models.CharField(max_length=255)
    cover_letter = models.TextField()
    class Meta:
        app_label = 'home'

class Photos(models.Model):
    image = models.ImageField(upload_to=upload_review_photo, blank=True, default=None, null=True)
class Video(models.Model):
    video = models.TextField( default=None, null=True, blank=True)

class Faqs(models.Model):
    question = models.CharField(max_length=255)
    answer = TextField(blank=False, null=False)

class Dealer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()

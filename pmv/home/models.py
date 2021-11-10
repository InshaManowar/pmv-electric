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
        verbose_name = 'Career query'
        verbose_name_plural = 'Career queries'

class Photos(models.Model):
    image = models.ImageField(upload_to=upload_review_photo, blank=True, default=None, null=True)
    class Meta:
        verbose_name = 'Photos'
        verbose_name_plural = 'Photos'

class Video(models.Model):
    video = models.TextField( default=None, null=True, blank=True)
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'



class Faqs(models.Model):
    question = models.CharField(max_length=255)
    answer = TextField(blank=False, null=False)

class Dealer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()

    class Meta:
        verbose_name = 'Dealer Query'
        verbose_name_plural = 'Dealers Queries'


class Fleet(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    class Meta:
        verbose_name = 'Fleet Query'
        verbose_name_plural = 'Fleet Queries'



from typing import Text
from django.db import models
from django.db.models.fields import EmailField, TextField
from embed_video.fields import EmbedVideoField

def upload_location(instance, filename):
	file_path = 'career/{name}-{filename}'.format(
     name=str(instance.name), filename=filename)
	return file_path

contact_subject = (
    ('Customer Enquiry', 'Customer Enquiry'),
    ('Vendor Enquiry', 'Vendor Enquiry'),
    ('Press Coverage', 'Press Coverage'),
    ('Investors', 'Investors'),
    ('Others', 'Others')
)

career = (
    ('Accounts', 'Accounts'),
    ('Administration', 'Administration'),
    ('Human Resources', 'Human Resources'),
    ('Technical', 'Technical'),
    ('Sales', 'Sales')
)

country = (
    ('USA', "United States of America"),
)
about_us = (
    ('facebook', "facebook"),
    ('instagram', "instagram"),
    ('linkedIn', "linkedIn"),
    ('YouTube', "YouTube"),
    ('Friend', "Friend"),
    ('News Article', "News Article"),
    ('Saw one on the street', "Saw one on the street"),
    ('Self Research/Browsing', "Self Research/Browsing"),
    ('Conference', "Conference"),
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
    resume = models.FileField(upload_to=upload_location, default=None)

    class Meta:
        app_label = 'home'
        verbose_name = 'Career query'
        verbose_name_plural = 'Career queries'

class Photos(models.Model):
    image = models.ImageField(upload_to=upload_review_photo, blank=True, default=None, null=True)

    class Meta:
        verbose_name = 'Photos'
        verbose_name_plural = 'Photos'

class Item(models.Model):
    video = EmbedVideoField() #




class Dealer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()

    class Meta:
        verbose_name = 'Dealer Query'
        verbose_name_plural = 'Dealers enquiries'
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, choices=contact_subject, blank=True, default=None)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural ='Contact us'
class Interest(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()

    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'


class Fleet(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    class Meta:
        verbose_name = 'Fleet Query'
        verbose_name_plural = 'Fleet enquiries'







class Reserve(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)

    

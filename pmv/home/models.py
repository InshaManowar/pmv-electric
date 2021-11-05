from django.db import models


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
        verbose_name = 'Career Request'

class Photos(models.Model):
    image = models.ImageField(upload_to=upload_review_photo, blank=True, default=None, null=True)
class Video(models.Model):
    video = models.TextField( default=None, null=True, blank=True)

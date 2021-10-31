from django.db import models


career = (
    ('Accounts', 'Accounts'),
    ('Administration', 'Administration'),
    ('Human Resources', 'Human Resources'),
    ('Technical', 'Technical'),
    ('Sales', 'Sales')
)

# Create your models here.
class CareerRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    interest = models.CharField(max_length=255, choices=career, default=None)
    position = models.CharField(max_length=255)
    cover_letter = models.TextField()

    class Meta:
        verbose_name = 'Career Request'
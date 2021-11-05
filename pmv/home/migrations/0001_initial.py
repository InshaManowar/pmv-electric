# Generated by Django 3.2.8 on 2021-11-02 19:13

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('interest', models.CharField(choices=[('Accounts', 'Accounts'), ('Administration', 'Administration'), ('Human Resources', 'Human Resources'), ('Technical', 'Technical'), ('Sales', 'Sales')], default=None, max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('cover_letter', models.TextField()),
            ],
            options={
                'verbose_name': 'Career Request',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=home.models.upload_review_photo)),
                ('vid', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]

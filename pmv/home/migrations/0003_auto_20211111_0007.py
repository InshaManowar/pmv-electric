# Generated by Django 3.2.8 on 2021-11-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dealer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Fleet Query',
                'verbose_name_plural': 'Fleet Queries',
            },
        ),
        migrations.AlterModelOptions(
            name='careerrequest',
            options={'verbose_name': 'Career query'},
        ),
        migrations.AlterModelOptions(
            name='dealer',
            options={'verbose_name': 'Dealer Query', 'verbose_name_plural': 'Dealers Queries'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name': 'Photos', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]

# Generated by Django 2.2 on 2024-08-07 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='description',
        ),
    ]

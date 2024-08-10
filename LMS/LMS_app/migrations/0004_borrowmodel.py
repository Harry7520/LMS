# Generated by Django 2.2 on 2024-08-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_app', '0003_auto_20240808_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrowModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=100)),
                ('b_image', models.ImageField(upload_to='')),
                ('s_name', models.CharField(max_length=100)),
                ('s_image', models.ImageField(upload_to='')),
                ('s_id', models.IntegerField(default=None)),
                ('s_gender', models.CharField(max_length=20)),
                ('s_grade', models.CharField(max_length=20)),
                ('s_phone', models.CharField(max_length=20)),
                ('s_email', models.EmailField(max_length=254)),
                ('s_address', models.TextField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

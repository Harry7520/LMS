# Generated by Django 2.2 on 2024-08-08 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_app', '0010_delete_studentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(default=None)),
                ('image', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('status', models.CharField(default='Disactive', max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='LMS_app.genderModel')),
                ('grade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='LMS_app.gradeModel')),
            ],
        ),
    ]

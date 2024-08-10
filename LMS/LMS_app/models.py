from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class bookModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class borrowModel(models.Model):
    b_name = models.CharField(max_length=100)
    b_image = models.ImageField()
    s_name = models.CharField(max_length=100)
    s_image = models.ImageField()
    s_id = models.IntegerField(default=None)
    s_gender = models.CharField(max_length=20)
    s_grade = models.CharField(max_length=20)
    s_phone = models.IntegerField(default=None)
    s_email = models.EmailField()
    s_address = models.TextField(max_length=200)
    status = models.CharField(max_length=20,default='Borrow')
    deadline = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.s_name} to {self.b_name}'
    
class genderModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class gradeModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class studentModel(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(default=None)
    image = models.ImageField()
    gender = models.ForeignKey(genderModel,on_delete=models.CASCADE,default=None)
    grade = models.ForeignKey(gradeModel,on_delete=models.CASCADE,default=None)
    email = models.EmailField()
    phone = models.IntegerField(default=None)
    address = models.TextField(max_length=200)
    status = models.CharField(max_length=20,default='Disactive')
    create_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.name
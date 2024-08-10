from django.contrib import admin
from LMS_app.models import *

# Register your models here.

admin.site.register(bookModel)
admin.site.register(studentModel)
admin.site.register(borrowModel)
admin.site.register(genderModel)
admin.site.register(gradeModel)
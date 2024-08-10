from django.urls import path
from LMS_app.views import *

urlpatterns =[
    path('home/', home , name='home'),
    path('student/add/', studentAdd),
    path('student/list/', studentList,name='student'),
    path('student/edit/<int:id>/', studentEdit),
    path('student/delete/<int:id>/', studentDelete),
    path('book/add/', bookAdd),
    path('book/list/', bookList, name='book'),
    path('book/delete/<int:id>/', bookDelete),
    path('borrow/list/', borrowList, name='borrow'),
    path('borrow/detail/<int:id>/', borrowDetail),
    path('borrow/delete/<int:id>/', borrowDelete),
    path('borrow/add/<int:b_id>/<int:s_id>/', borrowAdd),
    path('select/student/<int:b_id>/', select_student),
    path('search_by/', search_by),
    path('search_by1/', search_by1),
    path('search_by2/', search_by2),
    path('returning/<int:s_id>/<str:b_id>/<int:br_id>/', returning),
]
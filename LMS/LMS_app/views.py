from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from LMS_app.models import *
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def custom_404(request):
    return render(request,"404.html")

def to_login(request):
    return redirect('login')

def login_view(request):
    if request.method == "GET":
        return render(request , 'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')        
        else:
            messages.error(request,'Username or Password was wrong!')
            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    book = bookModel.objects.all()
    student = studentModel.objects.all()
    borrow = borrowModel.objects.all()
    return render(request,"home.html",{'book':book,'student':student,'borrow':borrow})

@login_required(login_url='login')
def studentAdd(request):
    if request.method == "GET":
        gender = genderModel.objects.all()
        grade = gradeModel.objects.all()
        return render(request,"student_add.html",{'gender':gender,'grade':grade})
    elif request.method == "POST":
        email = request.POST.get('email')
        student_id = request.POST.get('student_id')
        if studentModel.objects.filter(email=email).exists():
            messages.error(request,'User has been already existed!')
            return redirect('/student/add/')
        elif studentModel.objects.filter(student_id=student_id).exists():
            messages.error(request,'User has been already existed!')
            return redirect('/student/add/')
        else:
            name = request.POST.get('name')
            image = request.FILES.get('image')
            gender_id = request.POST.get('gender')
            grade_id = request.POST.get('grade')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            create_at = datetime.now()
            try:
                studentCreates = studentModel.objects.create(
                    name=name,
                    student_id=student_id,
                    image=image,
                    gender_id=gender_id,
                    grade_id=grade_id,
                    address=address,
                    email=email,
                    phone=phone,
                    create_at=create_at,
                )
                studentCreates.save()
                messages.success(request,'Student has been added successfully')
                return redirect('student')
            except Exception as e:
                messages.error(request,'Something was wrong!')
                return redirect('student')
        
@login_required(login_url='login')
def studentList(request):
    student = studentModel.objects.all()
    paginator = Paginator(student, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'student.html', {"student":page_obj})

@login_required(login_url='login')
def studentEdit(request,id):
    if request.method == "GET":
        student = studentModel.objects.get(id=id)
        gender = genderModel.objects.all()
        grade = gradeModel.objects.all()
        return render(request,"student_edit.html",{'student':student,'gender':gender,'grade':grade})
    elif request.method == "POST":
        student = studentModel.objects.get(id=id)
        student.name = request.POST.get('name')
        student.student_id = request.POST.get('student_id')
        student.gender_id = request.POST.get('gender')
        student.grade_id = request.POST.get('grade')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.phone = request.POST.get('phone')
        if request.FILES.get('image'):
            student.image.delete()
            student.image = request.FILES.get('image')
        student.save()
        messages.success(request,'Studend has been edited successfully')
        return redirect('student')

@login_required(login_url='login')
def studentDelete(request,id):
    student = studentModel.objects.get(id=id)
    student.image.delete()
    student.delete()
    messages.success(request,'Student has been deleted successfully')
    return redirect('student')

@login_required(login_url='login')
def bookAdd(request):
    if request.method == "GET":
        return render(request,"book_add.html")
    elif request.method == "POST":
        try:
            bookCreates = bookModel.objects.create(
                name = request.POST.get('name'),
                image = request.FILES.get('image'),
                create_at = datetime.now(),
            )
            bookCreates.save()
            messages.success(request,'Book has been added successfully')
            return redirect('book')
        except Exception as e:
            messages.error(request,'Something was wrong!')
            return redirect('book')

@login_required(login_url='login')
def bookList(request):
    book = bookModel.objects.filter(status=True)
    return render(request,"book.html",{'book':book})

@login_required(login_url='login')
def bookDelete(request,id):
    book = bookModel.objects.get(id=id)
    book.image.delete()
    book.delete()
    messages.success(request,'Book has been deleted successfully')
    return redirect('book')

@login_required(login_url='login')
def borrowList(request):
    borrow = borrowModel.objects.all()
    paginator = Paginator(borrow, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'borrow.html', {"borrow":page_obj})

@login_required(login_url='login')
def borrowDetail(request,id):
    borrow = borrowModel.objects.get(id=id)
    return render(request,"borrow_detail.html",{'borrow':borrow})

@login_required(login_url='login')
def borrowDelete(request,id):
    borrow = borrowModel.objects.get(id=id)
    borrow.s_image.delete()
    borrow.b_image.delete()
    borrow.delete()
    messages.success(request,'Borrow-List has been deleted successfully')
    return redirect('borrow')

@login_required(login_url='login')
def borrowAdd(request,b_id,s_id):
    if request.method == "GET":
        book = bookModel.objects.get(id=b_id)
        student = studentModel.objects.get(id=s_id)
        return render(request,"borrow_add.html",{'book':book,'student':student})
    elif request.method == "POST":
        book = bookModel.objects.get(id=b_id)
        student = studentModel.objects.get(id=s_id)
        borrowCreates = borrowModel.objects.create(
            b_name = book.name,
            b_image = book.image,
            s_name = student.name,
            s_image = student.image,
            s_id = student.student_id,
            s_gender = student.gender.name,
            s_grade = student.grade.name,
            s_email = student.email,
            s_address = student.address,
            s_phone = student.phone,
            deadline = request.POST.get('deadline'),
            create_at = datetime.now(),
        )
        borrowCreates.save()
        student.status = 'Active'
        student.save()
        book.status = False
        book.save()
        messages.success(request,'Book has been borrowed successfully')
        return redirect('borrow')

@login_required(login_url='login')
def search_by(request):
    search = request.GET.get('search')
    if search:
        book = bookModel.objects.filter(
            Q(name__icontains=search)
        )
        return render(request, 'book.html', {'book': book})
    else:
        book = bookModel.objects.all().order_by('create_at')
        return render(request, 'book.html', {'book': book})

@login_required(login_url='login')
def search_by1(request):
    search = request.GET.get('search')
    if search:
        student = studentModel.objects.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search)
        )
        paginator = Paginator(student, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'student.html', {'student': page_obj})
    else:
        student = studentModel.objects.all().order_by('create_at')
        paginator = Paginator(student, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'student.html', {'student': page_obj})

@login_required(login_url='login')
def search_by2(request):
    search = request.GET.get('search')
    if search:
        borrow = borrowModel.objects.filter(
            Q(b_name__icontains=search) |
            Q(s_name__icontains=search)
        )
        paginator = Paginator(borrow, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'borrow.html', {'borrow': page_obj})
    else:
        borrow = borrowModel.objects.all().order_by('create_at')
        paginator = Paginator(borrow, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'borrow.html', {'borrow': page_obj})

@login_required(login_url='login')
def select_student(request,b_id):
    book = bookModel.objects.get(id=b_id)
    student = studentModel.objects.all()
    return render(request,"select_student.html",{'book':book,'student':student})

@login_required(login_url='login')
def returning(request,s_id,b_id,br_id):
    student = studentModel.objects.get(student_id=s_id)
    book = bookModel.objects.get(name=b_id)
    borrow = borrowModel.objects.get(id=br_id)
    student.status = 'Disactive'
    student.save()
    book.status = True
    book.save()
    borrow.status = 'Return'
    borrow.save()
    return redirect('borrow')
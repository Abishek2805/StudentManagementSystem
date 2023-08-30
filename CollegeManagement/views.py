from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from CollegeManagement.models import City, Student


# Create your views here.
def base_fun(request):
    return render(request,'base.html')


def signup_fun(request):
    if request.method == "POST":
        name = request.POST['txtname']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(Q(username=name) | Q(email=email)).exists():
            data = {"msg": True}
            return render(request, 'signin.html', data)
        else:
            u1 = User.objects.create_superuser(username=name, password=password, email=email)
            u1.save()
            # return render(request,'login.html')
            return redirect('login')
    return render(request,'signin.html', {'msg': False})
    #
    # return render(request,'signup.html')


def login_fun(request):
    if request.method == "POST":
        name = request.POST['txtname']
        password = request.POST['password']
        user = authenticate(username=name, password=password)

        if user is not None:
            if user.is_superuser:
                return render(request,'home.html')
            else:
                data = {"msg": True}
                return render(request, 'login.html', data)
        else:
            data = {"msg": True}
            return render(request, 'login.html', data)
    else:
        return render(request, 'login.html', {'msg': False})
def home_fun(request):
    return render(request,'home.html')

def add_fun(request):
    c1 = City.objects.all()
    if request.method == 'POST':
        s1 = Student()
        s1.Name = request.POST['txtname']
        s1.place = City.objects.get(place=request.POST['ddlcity'])
        s1.MobileNumber = request.POST['txtnum']
        s1.Age = request.POST['txtnum1']
        s1.Email = request.POST['email']
        s1.Gender = request.POST['gender']
        s1.save()
        return render(request, 'thankyou.html')
    return render(request,'add.html',{'place':c1})


def display_fun(request):
    d1=Student.objects.all()
    return render(request,'display.html',{"data":d1})



def logout_fun(request):
    return render(request,'base.html')


def update_fun(request,id):
    c1 = City.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.Name = request.POST['txtname']
        s1.place = City.objects.get(place=request.POST['ddlcity'])
        s1.MobileNumber = request.POST['txtnum']
        s1.Age = request.POST['txtnum1']
        s1.Email = request.POST['email']
        s1.Gender = request.POST['gender']
        s1.save()
        return redirect('display')
    return render(request, 'update.html', {"d_data": s1,"data":c1})


def delete_fun(request,id):
    c1 = Student.objects.get(id=id)
    c1.delete()
    return redirect('display')
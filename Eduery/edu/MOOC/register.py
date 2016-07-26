from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from MOOC.models import *
from MOOC.admin import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

#学生进行注册
def registerstudent(request):    
    if request.method == "POST":
        uf = UserFormStudent(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password2 = uf.cleaned_data['password2']
            email = uf.cleaned_data['email']
            name = uf.cleaned_data['name']
            school = uf.cleaned_data['school']
            studentnum = uf.cleaned_data['studentnum']
            selfintroduction = uf.cleaned_data['selfintroduction']
            test = UserInfo.objects.filter(username__exact = username)
            if test.__len__() != 0:
                uf = UserFormStudent()
                return render_to_response('registration/registerstudent.html',{'ufstu':uf})
            if (not password) or (not password2) or (password != password2):
                uf = UserFormStudent()
                return render_to_response('registration/registerstudent.html',{'ufstu':uf})
            #将表单写入数据库
            user = UserInfo()
            user.username = username
            user.password = password
            user.email = email
            user.name = name
            user.school = school
            user.studentnum = studentnum
            user.selfintroduction = selfintroduction
            user.Type = 'student'#类型是学生
            user.save()
            userindjango = User.objects.create_user(username, email, password)
            userindjango.save()
            Userdjango = authenticate(username=username, password=password)
            auth.login(request, Userdjango)

            courses = Course.objects.all()
            categories = Category.objects.all()
            courseforuser = user.CourseList.all()
    
            return render_to_response('homepage/homepage.html',{'username':username, 'name':name, 'school':school, 'studentnum':studentnum, 'Type':'student', 'selfintroduction':selfintroduction, 'courses' : courses, 'categories': categories, 'courseforuser': courseforuser})
            #返回注册成功页面
    else:
        uf = UserFormStudent()
    return render_to_response('registration/registerstudent.html',{'ufstu':uf})





#教师进行注册
def registerteacher(request):
    if request.method == "POST":
        uf = UserFormTeacher(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password2 = uf.cleaned_data['password2']
            email = uf.cleaned_data['email']
            name = uf.cleaned_data['name']
            school = uf.cleaned_data['school']
            teachernum = uf.cleaned_data['teachernum']
            selfintroduction = uf.cleaned_data['selfintroduction']
            test = UserInfo.objects.filter(username__exact = username)
            if test.__len__() != 0:
                uf = UserFormTeacher()
                return render_to_response('registration/registerteacher.html',{'uftea':uf})
            if (not password) or (not password2) or (password != password2):
                uf = UserFormTeacher()
                return render_to_response('registration/registerteacher.html',{'uftea':uf})
            user = UserInfo()
            user.username = username
            user.password = password
            user.email = email
            user.name = name
            user.school = school
            user.teachernum = teachernum
            user.selfintroduction = selfintroduction
            user.Type = 'teacher'#类型是教师
            user.save()
            userindjango = User.objects.create_user(username, email, password)
            userindjango.save()
            Userdjango = authenticate(username=username, password=password)
            auth.login(request, Userdjango)
            #返回注册成功页面
            return render_to_response('homepage/homepageteacher.html',{'username':username, 'name':name, 'school':school, 'teachernum':teachernum, 'Type':'teacher', 'selfintroduction':selfintroduction})
    else:
        uf = UserFormTeacher()
    return render_to_response('registration/registerteacher.html',{'uftea':uf})








#学校进行注册
def registerschool(request):
    if request.method == "POST":
        uf = UserFormSchool(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password2 = uf.cleaned_data['password2']
            email = uf.cleaned_data['email']
            school = uf.cleaned_data['school']
            test = UserInfo.objects.filter(username__exact = username)
            if test.__len__() != 0:
                uf = UserFormSchool()
                return render_to_response('registration/registerschool.html',{'ufsch':uf})
            if (not password) or (not password2) or (password != password2):
                uf = UserFormSchool()
                return render_to_response('registration/registerschool.html',{'ufsch':uf})
            #将表单写入数据库
            user = UserInfo()
            user.username = username
            user.password = password
            user.email = email
            user.school = school
            user.Type = 'school'#类型是学校
            user.save()
            userindjango = User.objects.create_user(username, email, password)
            userindjango.save()
            Userdjango = authenticate(username=username, password=password)
            auth.login(request, Userdjango)
            #返回注册成功页面
            return render_to_response('homepage/homepageschool.html',{'username':username, 'school':school, 'Type':'school'})
    else:
        uf = UserFormSchool()
    return render_to_response('registration/registerschool.html',{'ufsch':uf})




def homepage(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request, 'homepage/homepage.html', {'username':'null', 'courses' : courses, 'categories': categories})




#登陆界面的选择身份界面（学生教师学校）
def register(request):
    return render(request, 'registration/register.html', {})


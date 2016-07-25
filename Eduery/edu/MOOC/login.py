from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from MOOC.models import *
from MOOC.admin import *


# 其他用户的注册
def login(request):
    if request.method == 'POST':
        ufl = UserLogForm(request.POST)
        if ufl.is_valid():
            #获取表单用户密码
            username = ufl.cleaned_data['username']
            password = ufl.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = UserInfo.objects.filter(username__exact=username,password__exact=password)
            #返回对应数据库内容的对象
            User = authenticate(username=username,password=password)
            #返回django自带的user
            if user and User:
                if User.is_active:
                      auth.login(request,User)
                if user[0].Type == 'student':
                    return render_to_response('homepage/homepage.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'studentnum':user[0].studentnum, 'Type':'student', 'selfintroduction':user[0].selfintroduction})
                elif user[0].Type == 'teacher':
                    return render_to_response('homepage/homepageteacher.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'teachernum':user[0].teachernum, 'Type':'teacher', 'selfintroduction':user[0].selfintroduction})
                elif user[0].Type == 'school':
                    return render_to_response('homepage/homepageschool.html',{'username':user[0].username, 'school':user[0].school, 'Type':'school'})
            else:
                return HttpResponseRedirect('/login/')
    else:
        ufl = UserLogForm()
    return render_to_response('registration/login.html',{'ufl':ufl})


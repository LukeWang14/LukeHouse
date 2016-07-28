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

def changeselfinformation(request):
    if not request.user.is_authenticated(): 
        return render_to_response("registration/register.html",{})
    form =  ChangeSelfInformationForm()     
    if request.method=="POST": 
        form =  ChangeSelfInformationForm(request.POST.copy()) 
        if form.is_valid(): 
            username = request.user.username 
            selfintroduction = form.cleaned_data["selfintroduction"] 
            user = UserInfo.objects.filter(username__exact = username)
            if user.__len__() == 0:
                 return render_to_response("registration/changeselfinformation.html",{'form':form}) 
            user[0].selfintroduction = selfintroduction 
            user[0].save()
            if user[0].Type == 'student':
                courses = Course.objects.all()
                categories = Category.objects.all()
                courseforuser = user[0].CourseList.all()
                return render_to_response('homepage/homepage.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'studentnum':user[0].studentnum, 'Type':'student', 'selfintroduction':user[0].selfintroduction, 'courses': courses, 'categories': categories, 'courseforuser': courseforuser})
            elif user[0].Type == 'teacher':
                courseforuser = user[0].CourseList.all()
                return render_to_response('homepage/homepageteacher.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'teachernum':user[0].teachernum, 'Type':'teacher', 'selfintroduction':user[0].selfintroduction, 'teaprofession': user[0].TeaProfession,'courseforuser': courseforuser})    
    return render_to_response("registration/changeselfinformation.html",{'form':form}) 

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

def changepassword(request):
    if not request.user.is_authenticated(): 
        return render_to_response("registration/register.html",{})
    form =  ChangePasswordForm()     
    if request.method=="POST": 
        form =  ChangePasswordForm(request.POST.copy()) 
        if form.is_valid(): 
            username = request.user.username 
            oldpassword = form.cleaned_data["oldpassword"] 
            newpassword1 = form.cleaned_data["newpassword1"] 
            newpassword2 = form.cleaned_data["newpassword2"]
            user = UserInfo.objects.filter(username__exact = username,password__exact = oldpassword)
            userdjango = authenticate(username=username,password=oldpassword) 
            if user: #原口令正确 
                if newpassword1 == newpassword2:#两次新口令一致 
                    userdjango.set_password(newpassword1)
                    userdjango.save()
                    auth.login(request, userdjango)
                    user[0].password = newpassword1
                    user[0].save()#修改密码后重新登录
                    if user[0].Type == 'student':
                        return render_to_response('homepage/homepage.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'studentnum':user[0].studentnum, 'Type':'student', 'selfintroduction':user[0].selfintroduction})
                    elif user[0].Type == 'teacher':
                        return render_to_response('homepage/homepageteacher.html',{'username':user[0].username, 'name':user[0].name, 'school':user[0].school, 'teachernum':user[0].teachernum, 'Type':'teacher', 'selfintroduction':user[0].selfintroduction})
                    elif user[0].Type == 'school':
                        return render_to_response('homepage/homepageschool.html',{'username':user[0].username, 'school':user[0].school, 'Type':'school'})
                else:#两次新口令不一致 
                    return render_to_response("registration/changepassword.html",{'form':form})  
            else:  #原口令不正确 
                if newpassword1 == newpassword2:#两次新口令一致 
                    return render_to_response("registration/changepassword.html",{'form':form}) 
                else:#两次新口令不一致            
                    return render_to_response("registration/changepassword.html",{'form':form})        
    return render_to_response("registration/changepassword.html",{'form':form}) 

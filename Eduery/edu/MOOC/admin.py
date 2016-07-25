from django.contrib import admin
from django import forms
from django.db import models
from .models import *

admin.site.register(Note)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(UserInfo)
admin.site.register(Question)
admin.site.register(Answer)

class UserFormStudent(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次输入密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：',max_length=100)
    name = forms.CharField(label='真实姓名：',max_length=100)
    school = forms.CharField(label='所在学校：',max_length=100)
    studentnum = forms.CharField(label='学生学号：',max_length=100)
    selfintroduction = forms.CharField(label='个人简介：',max_length=400)

class UserFormTeacher(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次输入密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：',max_length=100)
    name = forms.CharField(label='真实姓名：',max_length=100)
    school = forms.CharField(label='所在学校：',max_length=100)
    teachernum = forms.CharField(label='教师编号：',max_length=100)
    selfintroduction = forms.CharField(label='个人简介：',max_length=400)

class UserFormSchool(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次输入密码：',widget=forms.PasswordInput())
    email = forms.CharField(label='电子邮件：',max_length=100)
    school = forms.CharField(label='学校名称：',max_length=100)



 
    
    
class UserLogForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())



class ChangeSelfInformationForm(forms.Form):
    selfintroduction = forms.CharField(label='个人简介：',max_length=400)







    

class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"原密码",
            }
        ),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"新密码",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangePasswordForm, self).clean()
        return cleaned_data

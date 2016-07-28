from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *
from MOOC.login import *

def schoolcourse(request):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	username = request.user.username
	user = UserInfo.objects.filter(username__exact=username)
	if user:
		courseforuser = user[0].CourseList.all()
	return render(request, 'school_course.html', {'courseforuser': courseforuser})

def schoolstudent(request):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	username = request.user.username
	user = UserInfo.objects.filter(username__exact=username)
	username = user[0].username
	studentinschool = UserInfo.objects.filter(school__exact=username, Type__exact='student')
	studentinschoolcount = studentinschool.count()
	return render(request, 'homepage/homepageschool.html', {'username': username,'studentinschool': studentinschool, 'studentinschoolcount': studentinschoolcount})

def schoolteacher(request):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	username = request.user.username
	user = UserInfo.objects.filter(username__exact=username)
	teacherinschool = UserInfo.objects.filter(school__exact=username, Type__exact='teacher')
	teacherinschoolcount = teacherinschool.count()
	return render(request, 'school_teacher.html', {'teacherinschool': teacherinschool, 'teacherinschoolcount': teacherinschoolcount})

def student_show(request, student_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	student = UserInfo.objects.get(pk=student_id)
	username = student.name
	studentcourse = student.CourseList.all()
	studentcoursecount = studentcourse.count()
	return render(request, 'student.html', {'username': username,'student': student, 'studentcourse': studentcourse, 'studentcoursecount': studentcoursecount})

def student_delete(request, student_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	student = UserInfo.objects.get(pk=student_id)
	student.school = 'null'
	student.save()
	username = request.user.username
	studentinschool = UserInfo.objects.filter(school__exact=username, Type__exact='student')
	studentinschoolcount = studentinschool.count()
	return render(request, 'homepage/homepageschool.html', {'student': student, 'studentinschool': studentinschool, 'studentinschoolcount': studentinschoolcount})


def teacher_show(request, teacher_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	teacher = UserInfo.objects.get(pk=teacher_id)
	teachercourse = teacher.CourseList.all()
	teachercoursecount = teachercourse.count()
	return render(request, 'teacher.html', {'teacher': teacher, 'teachercourse': teachercourse, 'teachercoursecount': teachercoursecount})

def teacher_delete(request, teacher_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	teacher = UserInfo.objects.get(pk=teacher_id)
	teacher.school = 'null'
	teacher.save()
	username = request.user.username
	teacherinschool = UserInfo.objects.filter(school__exact=username, Type__exact='teacher')
	teacherinschoolcount = teacherinschool.count()
	return render(request, 'school_teacher.html', {'teacher': teacher, 'teacherinschool': teacherinschool, 'teacherinschoolcount': teacherinschoolcount})
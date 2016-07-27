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
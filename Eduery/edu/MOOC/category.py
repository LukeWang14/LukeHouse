from django.shortcuts import render
from django import forms
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *

def category(request, category_id):
	category = Category.objects.get(pk=category_id)
	courses = Course.objects.all()
	categories = Category.objects.all()
	categorycourse = Course.objects.filter(Type__pk = category_id)
	username = request.user.username
	courseforuser = UserInfo.objects.get(username__exact = username).CourseList.all();
	return render(request, 'homepage/homepage.html', {'courses': courses, 'categories': categories, 'category': category, 'courseforuser': courseforuser})
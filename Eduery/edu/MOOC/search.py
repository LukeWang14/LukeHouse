from django.shortcuts import render
from django.db.models import Q
from django import forms
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *

def searchcourse(request, search_content):
	courses = Course.objects.all().order_by('Type')
	categories = Category.objects.all()
	searchcourses = Course.objects.filter(Q(Name__icontains = search_content)|Q(InSchool__username__icontains = search_content)).order_by('Type')
	username = request.user.username
	courseforuser = UserInfo.objects.get(username__exact = username).CourseList.all();
	return render(request, 'homepagesearch.html', {'courses': courses, 'categories': categories, 'searchcourses': searchcourses, 'search_content': search_content, 'courseforuser': courseforuser})

def searchcoursecategory(request, search_content, category_id):
	courses = Course.objects.all().order_by('Type')
	categories = Category.objects.all()
	category = Category.objects.get(pk = category_id)
	username = request.user.username
	courseforuser = UserInfo.objects.get(username__exact = username).CourseList.all();
	searchcourses = Course.objects.filter(Q(Name__icontains = search_content)|Q(InSchool__username__icontains = search_content)).order_by('Type')
	return render(request, 'homepagesearch.html', {'courses': courses, 'categories': categories, 'searchcourses': searchcourses, 'search_content': search_content, 'category': category, 'courseforuser': courseforuser})

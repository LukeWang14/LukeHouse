from django.shortcuts import render
from django.contrib import auth
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from MOOC.models import *
from MOOC.admin import *


#登出
def logout(request):
    auth.logout(request)
    return render_to_response('homepage/homepage.html',{'username':'null'})



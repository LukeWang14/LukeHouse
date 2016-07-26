from django.shortcuts import render
from .models import *

def index(request):
    posts = Post.objects.all()
    courses = Course.objects.all()

    return render(request, 'MOOC/index.html', {'posts': posts, 'courses': courses}) 
# Create your views here.

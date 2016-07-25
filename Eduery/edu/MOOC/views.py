from django.shortcuts import render
def index(request):
    posts = Post.objects.all()
    return render(request, 'MOOC/index.html', {'posts': posts}) 
# Create your views here.

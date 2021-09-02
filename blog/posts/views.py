from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):

    posts =  Post.objects.all()

    return render(request,'posts/index.html',{'posts':posts})

def post(request,pk):
    one_post = Post.objects.get(id=pk)
    return render(request,'posts/one_post.html',{'post':one_post})
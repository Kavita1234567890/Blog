from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Category

def home(request):
    # load post from db(10 - i want to show first 10 posts)
    post=Post.objects.all()[:11]
    
    cats = Category.objects.all()
    data = {'post':post, 'cats':cats}
    return render(request, 'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'post.html',{'post':post,'cats':cats})

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html',{'cat':cat,'posts':posts})
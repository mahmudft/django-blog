from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    return render(request, 'index.html')

def blogs(request):
    blog = Article.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'blog.html', context)


def about(request):
    return render(request, 'about.html')

def detail(request, id):
    detail_post = get_object_or_404(Article, id=id)
    context = {
        'post': detail_post
    }
    return render(request, 'detail.html', context)


from django.shortcuts import render
import datetime
from blog.models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.exclude(published_date__gt=datetime.date(2025, 1, 3))
    context = {'posts': posts}
    return render(request,'blog/blog-home.html' , context)
def blog_single(request , slug):
    cn=Post.objects.get(slug=slug)
    cn.counted_views+=1
    cn.save()
    post = Post.objects.get(slug=slug)

    context = {'post':post}
    return render(request,'blog/blog-single.html',context)
from django.shortcuts import render , get_object_or_404
import datetime
from blog.models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def blog_single(request , slug):
    cn=Post.objects.get(slug=slug)
    cn.counted_views += 1
    cn.save()
    post = get_object_or_404(Post, published_date__lt=datetime.datetime.now() , status=1 ,slug=slug)  # Post.objects.get()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)
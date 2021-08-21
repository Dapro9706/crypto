from .models import Post
from django.shortcuts import render


def riddle(request, r_id):
    try:
        p = Post.objects.get(name=r_id)
        return render (request,'r.html',context={'content':p.content})
    except Post.DoesNotExist:
        return render (request,'r.html',context={'content':'Invalid URL'})

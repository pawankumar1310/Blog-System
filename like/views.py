from re import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import ListView
from account.models import Usermodel
from blog.models import Blog
from like.models import Like
from django.urls import reverse
from django.shortcuts import redirect
from urllib import request
# Create your views here.

class LikeView(View):
    model = Blog
    def post(self,request,*args,**kwargs):
        blog_id= request.POST.get('blog_id')
        Blog_posts_obj = Blog.objects.get(pk = blog_id)
        if request.user not in Blog_posts_obj.likes.all():
            Blog_posts_obj.likes.add(request.user)
        else:
            Blog_posts_obj.likes.remove(request.user)
        like, created = Like.objects.get_or_create(user = request.user,  blog_post_id=blog_id )

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
        return redirect(request.META.get('HTTP_REFERER'))

class LikedPost(ListView):
    model = Blog
    template_name="components/favourite_post.html"
    def get_context_data(self,**kwargs):
        context = super(LikedPost,self).get_context_data(**kwargs)
        blog_post= Blog.objects.filter(likes = self.request.user)
        context.update({'posts':blog_post})
        return context





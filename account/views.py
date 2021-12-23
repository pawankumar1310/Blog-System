import re
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import datetime
from django.views.decorators.csrf import csrf_exempt
from account.models import Usermodel
from blog.models import Blog
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.http import Http404
from account.forms import SignUpForm
from blog.forms import PostForm
from notification.views import NotificationView
from django.contrib.auth.mixins import LoginRequiredMixin
from notification.models import Notification


class MyAccount(DetailView):
    model = Usermodel
    queryset = Usermodel.objects.prefetch_related()

    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            raise Http404()

        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add context data for posts made by the users

        if self.object.can_post:
            user_posts = Blog.objects.filter(author_id=self.object)
            context['posts'] = user_posts

        return context


class UserSignUpView(CreateView):
    template_name = 'signup.html'
    success_url = '/'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super(UserSignUpView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)
        self.object = form.save()
        login(request, self.object)
        return redirect('account:login')


class UserLogoutView(LogoutView):
    template_name = 'logout.html'


class UserLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        # If user already logged in redirect home

        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().get(request, **kwargs)


class UpdateProfile(UpdateView):
    model = Usermodel
    fields = ['bio']
    template_name = 'update_profile.html'
    success_url = '/account'

    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            raise Http404()
        return self.request.user


class MakePostView(LoginRequiredMixin, CreateView):
    template_name = 'post.html'
    success_url = '/'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.can_post:
            # Only logged in Authors and Moderators can post
            raise Http404("Page not found")
        return super(MakePostView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.can_post:
            # Only logged in Authors and Moderators can post
            raise Http404("Page not found")

        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)
        self.object = form.save()
        self.object.author_id = request.user

        content = "Created a new BlogPost"
        user_name = NotificationView.get_context_data(self)
        for user in user_name:
            users = Usermodel.objects.filter(pk=user)
            print(users)
            new_notification = Notification.objects.create(
                author=self.object.author_id, content=content, blogPost=self.object)
            new_notification.reader.set(users)
            new_notification.save()

        self.object.save()

        return redirect('blog:home')

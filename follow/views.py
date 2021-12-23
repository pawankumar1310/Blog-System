from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeDoneView
from django.shortcuts import redirect, render
from django.views.generic import ListView,View
from django.contrib.auth.models import User
from account.models import Usermodel
from django.http import HttpResponse,JsonResponse
from follow.models import Followers
import json
from django.db.models.query import QuerySet
from django.db.models import Q
# Create your views here
from urllib import request
User = get_user_model()

class followerscount(View):
    def post(self,request,*args,**kwargs):

        followed_user_id = request.POST.get('followed_user_id')
        print(followed_user_id)
        followed_user_obj = Usermodel.objects.get(pk = followed_user_id)
        try:
            Followers.objects.get(user = request.user,followed = followed_user_obj)
        except Exception as e:
            follow_obj = Followers.objects.create(followed = followed_user_obj)


        return redirect(request.META.get('HTTP_REFERER'))

class UnfollowCount(View):
    print("Entered")
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)
        try:
            
            follow_obj = Followers.objects.get(user=request.user, followed=unfollowed_user_obj)    
            follow_obj.delete()
        except Exception as e:
            pass
        

        return redirect(request.META.get('HTTP_REFERER'))
        
# to show all the favrouite Authors
class FavouriteAuthor(ListView):
    model = Usermodel
    template_name = 'components/favourite_author.html'

    def get_context_data(self, **kwargs):
        context = super(FavouriteAuthor, self).get_context_data(**kwargs)
        followers = Followers.objects.filter(user=self.request.user)
        context.update({'followers': followers,'reader':self.request.user})
        return context
        # return render(request, 'components/favourite_author.html', {'followers' : followers})

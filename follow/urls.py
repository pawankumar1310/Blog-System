from django.urls import path
from follow.views import  followerscount,UnfollowCount,FavouriteAuthor
from django.contrib.auth.decorators import login_required

app_name = 'follow'

urlpatterns = [

   path('follows/', login_required(followerscount.as_view()), name='followed'),
   path('follows_back/',login_required(UnfollowCount.as_view()), name = 'Unfollowed'),
   path('favourite_author/',login_required(FavouriteAuthor.as_view()),name = 'Liked_author')
]
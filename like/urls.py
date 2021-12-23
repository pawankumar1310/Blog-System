from django.contrib import admin
from django.urls import path
from like import views as like_views

app_name = 'like'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('like/',      like_views.LikeView.as_view(),  name='like_post'),
    path('likedPosts/',like_views.LikedPost.as_view(),  name='Liked_post'),
]
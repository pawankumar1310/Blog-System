from django.contrib import admin
from django.urls import path
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',    blog_views.BlogPostsView.as_view(),  name='home'),
    path('bloggers/', blog_views.BloggersList.as_view(),   name='bloggers'),
    path('search/',   blog_views.BlogSearchView.as_view(), name="search"),
    path('blog/<int:pk>', blog_views.BlogPostDetailView.as_view(), name='post'),
    path('author/<int:pk>', blog_views.AuthorPostsView.as_view(), name='author'),
]
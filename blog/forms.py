from django.forms import ModelForm

from blog.models import Blog


class PostForm(ModelForm):
    class Meta:
        model = Blog
        fields = (
            'blog_title',
            'blog_description',
            'blog_content',
            'blog_image'
        )
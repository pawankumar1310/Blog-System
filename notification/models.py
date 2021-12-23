from django.db import models
from account.models import Usermodel
from blog.models import Blog
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notification(models.Model):

    author = models.ForeignKey(Usermodel, related_name='author', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    blogPost = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    reader = models.ManyToManyField(Usermodel, related_name='reader')
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:50]





from django.db import models
from django.db.models.deletion import CASCADE
from urllib import request

from account.models import Usermodel
from blog.models import Blog

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(Usermodel, on_delete=models.CASCADE) #user could be both reader or author
    blog_post = models.ForeignKey(Blog,on_delete=CASCADE)
    value = models.CharField(choices=Blog.LIKE_CHOICE,default='Like',max_length=10)


    def __str__(self):
        return str(self.blog_post)



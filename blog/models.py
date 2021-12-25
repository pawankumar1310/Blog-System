from django.db import models
from account.models import  Usermodel
from category.models  import Category
from django.core.exceptions import ValidationError
from urllib import request



# Create your models here.


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100, null=True, default="")
    blog_description = models.TextField(max_length=1024)
    blog_content = models.TextField(max_length=2500, null=True, default="") 
    author_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True)
    blog_image = models.ImageField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='posts', blank=True)
    likes = models.ManyToManyField(Usermodel,related_name='blog_posts')


    class Meta:
        db_table = "blog"
        ordering = ["-created_time"]

    def __unicode__(self):
        return u'%s' % [self.blog_id]

    def is_liked(self):
        return Blog.objects.filter(likes = self.user).exists()



    @property
    def like_count(self):
        return self.likes.count()

    LIKE_CHOICE = (
        ('Like', 'Like'),
        ('Unlike','Unlike'),
    )

class UserComment(models.Model):
    author_id = models.ForeignKey(Usermodel, on_delete=models.SET_NULL, null=True, related_name='posts')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=512)
    comment_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if UserComment.objects.filter(author_id =self.author_id,blog_id=self.blog_id).count() < 3:
            return super(UserComment,self).save(*args,**kwargs)

        raise ValidationError("You have reached Comment limits")

    def __str__(self):
        return f'{self.author_id} {self.comment_date}'
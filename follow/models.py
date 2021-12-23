from django.contrib.auth import get_user
from django.db import models
from account.models import *
from django.db.models.deletion import CASCADE
from account.models import Usermodel
from follow.utils import auto_save_current_user




# Create your models here.
class Followers(models.Model):
    followed=models.ForeignKey(Usermodel,related_name = 'follow_followed',on_delete=models.CASCADE)
    user=models.ForeignKey(Usermodel, related_name = 'follow_follower',on_delete=models.CASCADE, editable=False)


    def __str__(self):
        return f"{self.user} --> {self.followed}"



    def save(self, *args,**kwargs):        
        auto_save_current_user(self)
        super(Followers, self).save(*args, **kwargs)

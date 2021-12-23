from django.contrib.auth.models import User
from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import render, render_to_response, redirect
from account.models import Usermodel
from notification.models import Notification
from django.views.generic import ListView
from follow.models import Followers
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.


class NotificationView(ListView):
    model = Notification
    template_name = 'notification.html'

    def get(self, request):
        # notis = request.user.notification_set.filter(is_read=False).order_by('-created')
        notis = Notification.objects.filter(
            reader=self.request.user, is_read=False).order_by('-created')
        context = ({'notice': notis})
        return render(request, "notification.html", context)

    def get_context_data(self):

        Follow_obj = Followers.objects.values_list(
            'user', flat=True).filter(followed=self.request.user)
        return Follow_obj

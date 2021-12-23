from django.urls import path   
from django.contrib.auth.decorators import login_required 

from notification.views import NotificationView
app_name = 'notification'

urlpatterns = [
    path('notification/',login_required(NotificationView.as_view()), name='notified'),
    
]
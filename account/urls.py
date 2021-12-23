from django.contrib import admin
from django.contrib.auth import views as admin_views
from django.urls import path
from account import views as account_views

app_name = 'account'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',       account_views.MyAccount.as_view(),        name='account'),
    path('signup/',account_views.UserSignUpView.as_view(), name='signup'),
    path('logout/',account_views.UserLogoutView.as_view(), name='logout'),
    path('login/', account_views.UserLoginView.as_view(),  name='login'),
    path('edit/',  account_views.UpdateProfile.as_view(), name='update_profile'),
    path('post/',  account_views.MakePostView.as_view(), name='new_post'),
]


urlpatterns += [
    path('password_change/', admin_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', admin_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', admin_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', admin_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', admin_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', admin_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
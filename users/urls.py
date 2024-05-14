from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *
app_name = 'users'


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

]

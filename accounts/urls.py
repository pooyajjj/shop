from django.urls import path
from accounts.views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('otp/<int:id>/', create_otp, name='otp')
]
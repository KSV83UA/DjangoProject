from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,  name='home'),
    # path('manager/', manager, name='manager'),
    path('manager_cabinet/', manager_cabinet, name='manager_cabinet'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout')
]
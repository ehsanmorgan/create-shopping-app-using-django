from django.urls import path
from .views import Home_List


app_name='home'

urlpatterns = [
    path('',Home_List,name='home_list')
]

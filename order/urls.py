from django.urls import path
from .views import order_List

app_name='order'

urlpatterns = [
    path('',order_List.as_view(),name='order'),
]

from django.urls import path
from .views import fashionlist,fashion_detail,electroniclist,electronic_detail


app_name='shop'


urlpatterns = [
    path('list',fashionlist.as_view(),name='fashion_list'),
    path('detail/<slug:slug>',fashion_detail.as_view(),name='fashion_detail'),
    path('electro_list',electroniclist.as_view(),name='electroniclist'),
    path('electro_detail/<slug:slug>',electronic_detail.as_view(),name='electronic_detail'),
]

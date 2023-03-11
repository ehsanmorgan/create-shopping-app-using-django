from django.urls import path
from .views import add_reviews,add_reviews1 ,fashionlist,fashion_detail,electroniclist,electronic_detail,jewellerylist,jewellery_detail,add_reviews2
from .api import elecrtonicListApi,elecrtonicDetailtApi,fashionListApi


app_name='shop'


urlpatterns = [
    path('list',fashionlist.as_view(),name='fashion_list'),
    path('detail/<slug:slug>',fashion_detail.as_view(),name='fashion_detail'),
    path('electro_list',electroniclist.as_view(),name='electroniclist'),
    path('<slug:slug>/add_review',add_reviews,name='add_review'),
    path('<slug:slug>/add_review1',add_reviews1,name='add_review1'),
    path('<slug:slug>/add_review2',add_reviews2,name='add_review2'),
    path('electro_detail/<slug:slug>',electronic_detail.as_view(),name='electronic_detail'),
    path('jewellery_list',jewellerylist.as_view(),name='jewellerylist'),
    path('jewellery_detail/<slug:slug>',jewellery_detail.as_view(),name='jewellery_detail'),
    
    
    
    
    #API
    path('api/list',elecrtonicListApi.as_view(),name='api-list'),
    path('api/list/<slug:slug>',elecrtonicDetailtApi.as_view(),name='productDetailApi-list'),
    path('api/fashionlist',fashionListApi.as_view(),name='api-fashionlist'),
]

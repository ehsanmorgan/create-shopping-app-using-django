from rest_framework.decorators import api_view
from rest_framework import generics
from .serializer import electronicListSerialize,electronicDetailSerialize
from .models import Electronic
from .myfilter import electroncFilter
import django_filters.rest_framework



class elecrtonicListApi(generics.ListAPIView):
    queryset=Electronic.objects.all() 
    serializer_class=electronicListSerialize 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields=['name','flag','price']
    filterset_class=electroncFilter
    
    
    
    
class elecrtonicDetailtApi(generics.RetrieveDestroyAPIView):
    queryset=Electronic.objects.all() 
    serializer_class=electronicDetailSerialize 
    lookup_field='slug'
    
    
 
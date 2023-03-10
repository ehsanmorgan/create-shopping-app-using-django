from rest_framework.decorators import api_view
from rest_framework import generics
from .serializer import electronicListSerialize,electronicDetailSerialize
from .models import Electronic



class elecrtonicListApi(generics.ListAPIView):
    queryset=Electronic.objects.all() 
    serializer_class=electronicListSerialize 
    
    
    
    
class elecrtonicDetailtApi(generics.RetrieveDestroyAPIView):
    queryset=Electronic.objects.all() 
    serializer_class=electronicDetailSerialize 
    lookup_field='slug'
    
    
 
from django_filters import rest_framework as filters

from .models import Electronic

class electroncFilter(filters.FilterSet):
    class Meta:
        model=Electronic
        fields={
            'name':['icontains'],
            'price':['lte','gte','range'],
            'quantity':['range'],
            'flag':['exact'],
            
        }
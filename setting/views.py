from django.shortcuts import render
from django.views.generic import ListView
from .models import home
from shop.models import Fashion,Electronic,Jewellery



# Create your views here.


def Home_List(request):
    fashion=Fashion.objects.all()[:3]
    electronic=Electronic.objects.all()[:3]
    jewellery=Jewellery.objects.all()[:3]
    
    return render(request,'home_list.html',{'fashion':fashion,'electronic':electronic,'jewellery':jewellery})
    
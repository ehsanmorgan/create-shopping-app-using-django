from django.shortcuts import render
from .models import Fashion

# Create your views here.







def fashionlist(request):
    fashion=Fashion.objects.all()
    return render(request,'fashion_list.html',{'fashion':fashion})



def fashion_detail(request,slug):
    fashion_1=Fashion.objects.get(slug=slug)
    return render (request,'fashion_detail.html',{'fashion_1':fashion_1})
    
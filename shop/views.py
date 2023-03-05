from django.shortcuts import render
from .models import Fashion
from django.views.generic import ListView,DetailView

# Create your views here.







class fashionlist(ListView):
    model=Fashion
    paginate_by = 9




def fashion_detail(request,slug):
    fashion_1=Fashion.objects.get(slug=slug)
    return render (request,'fashion_detail.html',{'fashion_1':fashion_1})
    
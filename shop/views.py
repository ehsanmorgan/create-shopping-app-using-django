from django.shortcuts import render
from .models import Fashion,Electronic,Jewellery
from django.views.generic import ListView,DetailView

# Create your views here.







class fashionlist(ListView):
    model=Fashion
    paginate_by = 18


class fashion_detail(DetailView):
    model=Fashion
    
    
    
    
    

class electroniclist(ListView):
    model=Electronic
    paginate_by = 18


class electronic_detail(DetailView):
    model=Electronic
    
    
    
    
    
    
    
class jewellerylist(ListView):
    model=Jewellery
    paginate_by = 18


class jewellery_detail(DetailView):
    model=Jewellery
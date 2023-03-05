from django.shortcuts import render
from .models import Fashion,Electronic
from django.views.generic import ListView,DetailView

# Create your views here.







class fashionlist(ListView):
    model=Fashion
    paginate_by = 9




class fashion_detail(DetailView):
    model=Fashion
    
    
    

class electroniclist(ListView):
    model=Electronic
    paginate_by = 9




class electronic_detail(DetailView):
    model=Electronic
    
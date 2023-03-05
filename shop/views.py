from django.shortcuts import render
from .models import Fashion
from django.views.generic import ListView,DetailView

# Create your views here.







class fashionlist(ListView):
    model=Fashion
    paginate_by = 9




class fashion_detail(DetailView):
    model=Fashion
    
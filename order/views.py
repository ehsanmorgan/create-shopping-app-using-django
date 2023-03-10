from django.shortcuts import render
from django.views.generic import ListView

from .models import order
# Create your views here.



class order_List(ListView):
    model=order

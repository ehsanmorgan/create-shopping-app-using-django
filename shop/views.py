from django.shortcuts import render,redirect
from .models import Fashion,Electronic,Jewellery,Reviews
from django.views.generic import ListView,DetailView
from .forms import commentform
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


def add_reviews(request,slug):
    add_comment=Electronic.objects.get(slug=slug)
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.electronic=add_comment
            myform.save()
            
    return redirect(f'/center/electro_detail/{add_comment.slug}')
        




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
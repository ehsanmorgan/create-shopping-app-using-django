from django.shortcuts import render,redirect
from .models import Fashion,Electronic,Jewellery,Reviews,Reviews1
from django.views.generic import ListView,DetailView
from .forms import commentform,fashionform
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
            
            
            
            reviews_1=Reviews.objects.filter(electronic=add_comment)
            html = render_to_string('include/add_allcomment.html',{'reviews_1':reviews_1 , request:request})
            return JsonResponse({'result':html})
            
            
            
            
def add_reviews1(request,slug):
    add_comment1=Fashion.objects.get(slug=slug)
    if request.method=='POST':
        form=fashionform(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.fashion=add_comment1
            myform.save()
            
            
            
            
            
            reviews_2=Reviews1.objects.filter(fashion=add_comment1)
            html = render_to_string('include/add_all2.html',{'reviews_2':reviews_2 , request:request})
            return JsonResponse({'result':html})
            
    





class fashionlist(ListView):
    model=Fashion
    paginate_by = 18


class fashion_detail(DetailView):
    model=Fashion
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews_2"] = Reviews1.objects.filter(fashion=self.get_object())
        return context
    
    
    
    
    

class electroniclist(ListView):
    model=Electronic
    paginate_by = 18


class electronic_detail(DetailView):
    model=Electronic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews_1"] = Reviews.objects.filter(electronic=self.get_object())
        return context
    
    
    
    
    
    
    
    
class jewellerylist(ListView):
    model=Jewellery
    paginate_by = 18


class jewellery_detail(DetailView):
    model=Jewellery
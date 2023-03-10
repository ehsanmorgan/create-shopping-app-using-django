from django import forms

from .models import Reviews,Reviews1,Reviews_Jewellery

class commentform(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['comment']
        
        
        
class fashionform(forms.ModelForm):
    class Meta:
        model=Reviews1
        fields=['comment1']
        
        
        
class jewelleryform(forms.ModelForm):
    class Meta:
        model=Reviews_Jewellery
        fields=['comment2']
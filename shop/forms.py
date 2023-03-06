from django import forms

from .models import Reviews

class commentform(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['comment']
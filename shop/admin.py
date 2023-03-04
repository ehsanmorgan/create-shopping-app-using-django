from django.contrib import admin

# Register your models here.
from .models import Fashion 



class fashionAdmin(admin.ModelAdmin):
    list_display=['id','title','price']
    list_filter=['price']
    list_editable=['title','price']
    search_fields=['title','price']
    
    



admin.site.register(Fashion,fashionAdmin)


# Register your models here.

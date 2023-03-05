from django.contrib import admin

# Register your models here.
from .models import Fashion 



class fashionAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']
    
    



admin.site.register(Fashion,fashionAdmin)


# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Fashion ,Electronic



class fashionAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']
    
    
    
class electronicAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']
    
    



admin.site.register(Fashion,fashionAdmin)
admin.site.register(Electronic,electronicAdmin)


# Register your models here.

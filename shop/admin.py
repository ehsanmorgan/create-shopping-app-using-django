from django.contrib import admin

# Register your models here.
from .models import Fashion ,Electronic,Jewellery,Reviews,Reviews1

class reviewAdmin(admin.ModelAdmin):
    list_display=['id','comment']
    list_filter=['comment']
    list_editable=['comment']
    search_fields=['comment']
    
    
class reviewAdmin1(admin.ModelAdmin):
    list_display=['id','comment1']
    list_filter=['comment1']
    list_editable=['comment1']
    search_fields=['comment1']

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
    
    
class jewelleryAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']



admin.site.register(Fashion,fashionAdmin)
admin.site.register(Electronic,electronicAdmin)
admin.site.register(Jewellery,jewelleryAdmin)
admin.site.register(Reviews,reviewAdmin)
admin.site.register(Reviews1,reviewAdmin1)


# Register your models here.

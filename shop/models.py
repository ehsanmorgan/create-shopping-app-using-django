from django.db import models
from django.utils.text import slugify

# Create your models here.

flag_chois=[
    ('English','English'),
    ('France','France'),
]

class Fashion(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='shoping/')
    price=models.FloatField()
    flag=models.CharField(choices=flag_chois,max_length=30)
    quantity=models.IntegerField(default=0)
    slug=models.SlugField(null=True,blank=True)
    
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Fashion,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
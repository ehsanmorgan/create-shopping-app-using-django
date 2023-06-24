from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

flag_chois=[
    ('English','English'),
    ('France','France'),
]

class Fashion(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='shoping/')
    price=models.FloatField()
    flag=models.CharField(choices=flag_chois,max_length=30)
    quantity=models.IntegerField(default=0)
    slug=models.SlugField(null=True,blank=True)
    
    
    
    
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Fashion,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
    
    
flag_chois=[
    ('English','English'),
    ('France','France'),
]

class Electronic(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='electronic/')
    price=models.FloatField()
    flag=models.CharField(choices=flag_chois,max_length=30)
    quantity=models.IntegerField(default=0)
    slug=models.SlugField(null=True,blank=True)
    
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Electronic,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
flag_chois=[
    ('English','English'),
    ('France','France'),
]

class Jewellery(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='jewellery/')
    price=models.FloatField()
    flag=models.CharField(choices=flag_chois,max_length=30)
    quantity=models.IntegerField(default=0)
    slug=models.SlugField(null=True,blank=True)
    
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Jewellery,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
    
    
class Reviews(models.Model):
    user=models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    electronic=models.ForeignKey(Electronic,related_name='review_electronic',on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)
    createt_at=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.comment
    
    
    
    
class Reviews1(models.Model):
    user1=models.ForeignKey(User,related_name='review_author1',on_delete=models.SET_NULL,null=True,blank=True)
    fashion=models.ForeignKey(Fashion,related_name='fashion_review',on_delete=models.CASCADE)
    comment1=models.TextField(max_length=200)
    createt_at1=models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self):
        return self.comment1
    
    
    
class Reviews_Jewellery(models.Model):
    user=models.ForeignKey(User,related_name='review_author2',on_delete=models.SET_NULL,null=True,blank=True)
    jewellery=models.ForeignKey(Jewellery,related_name='jewellery_review',on_delete=models.CASCADE)
    comment2=models.TextField(max_length=200)
    createt_at2=models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self):
        return self.comment2
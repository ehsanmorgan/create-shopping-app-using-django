from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/',default='default.png')
    


@receiver(post_save,sender=User)    
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance 
            
        )
        


class ContactNumber(models.Model):
    user=models.ForeignKey(User,related_name='user_number',on_delete=models.CASCADE)
    number=models.CharField(max_length=20)
    
    

class Adresse(models.Model):
    user=models.ForeignKey(User,related_name='user_adresse',on_delete=models.CASCADE)
    city=models.CharField(max_length=20)
    street=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    notes=models.CharField(max_length=20)
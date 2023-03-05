from django.db import models

# Create your models here.


class home(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='home')
    email_us=models.EmailField(max_length=30)
    about=models.TextField(max_length=1000)
    emails=models.CharField(max_length=30)
    phonse=models.CharField(max_length=30)
    adresse=models.CharField(max_length=30)


    def __str__(self):
        return self.name
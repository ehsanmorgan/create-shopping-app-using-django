from rest_framework import serializers
from .models import Electronic,Reviews,Fashion
from rest_framework.response import Response
import django_filters.rest_framework






class fashionSerializer(serializers.ModelSerializer):
    price_tex=serializers.SerializerMethodField('mynew_price')
    review_count=serializers.SerializerMethodField()
    class Meta:
        model=Fashion
        fields='__all__'
        
          
    def get_review_count(self,Fashion):
        rview=Fashion.fashion_review.all().count()
        return rview
        
        
    def mynew_price(self,Electronic):
        return Electronic.price*1.2



class electronicListSerialize(serializers.ModelSerializer):
    price_tex=serializers.SerializerMethodField('mynew_price')
    review_count=serializers.SerializerMethodField()
    
    class Meta:
        model=Electronic
        fields='__all__'
        
    def get_review_count(self,Electronic):
        rview=Electronic.review_electronic.all().count()
        return rview
        
        
    def mynew_price(self,Electronic):
        return Electronic.price*1.2
        
        
class reviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Reviews
        fields=['comment','user']    


class electronicDetailSerialize(serializers.ModelSerializer):
    price_tex=serializers.SerializerMethodField('mynew_price')
    review_count=serializers.SerializerMethodField()
    review=reviewSerializer(source='review_electronic',many=True)
    class Meta:
        model=Electronic
        fields='__all__'
        
          
    def mynew_price(self,Electronic):
        return Electronic.price*1.2
        
        
        
    def get_review_count(self,Electronic):
        rview=Electronic.review_electronic.all().count()
        return rview
    
    

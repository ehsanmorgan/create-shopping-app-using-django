from rest_framework import serializers
from .models import Electronic,Reviews



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
            


class electronicDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model=Electronic
        fields='__all__'
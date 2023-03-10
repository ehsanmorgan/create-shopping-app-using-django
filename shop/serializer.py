from rest_framework import serializers
from .models import Electronic



class electronicListSerialize(serializers.ModelSerializer):
    class Meta:
        model=Electronic
        fields='__all__'


class electronicDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model=Electronic
        fields='__all__'
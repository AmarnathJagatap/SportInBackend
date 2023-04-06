from rest_framework import serializers
from .models import Products

class ProductCreateSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ['id','title','discription','rate','category','dimension','image']
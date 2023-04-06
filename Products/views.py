from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,throttle_classes
from rest_framework.permissions import AllowAny, IsAuthenticated,\
    IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .serializers import ProductCreateSerialiser
from .models import Products
from rest_framework import generics


@api_view(['POST'])
def createnewProduct(request):
    serializer = ProductCreateSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"response" :  serializer.data})
    else:
        return Response(serializer.errors)

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductCreateSerialiser

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products
    serializer_class = ProductCreateSerialiser


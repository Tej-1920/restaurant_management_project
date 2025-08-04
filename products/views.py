from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''
class MenuView(APIView):
    def get(self,request):
        menu = [
            {"name":"Paneer Butter Masala","description":"Creamy cottage cheese curry","price":150},
            {"name":"Veg Biryani","description":"Spicy mixed vegatable rice","price":120},
            {"name":"Gulab Jamun","description":"Sweet dessert","price":50}
        ]
        return Response(menu,status=status.HTTP_200_OK)

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

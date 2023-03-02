from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MenuCardSerializer
from .models import MenuCard

# Create your views here.
@api_view(['POST'])
def AddMenu(request):
    serializer = MenuCardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def ViewMenu(request):
    menu = MenuCard.objects.all()
    serializer = MenuCardSerializer(menu, many = True)
    return Response(serializer.data)

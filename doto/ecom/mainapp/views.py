from django.shortcuts import render
from rest_framework import generics,status
from .serializers import dotoserializers
from .models import doto
from rest_framework.views import APIView
from rest_framework.response import Response


#CRUD operations

class dotoListAPIView(generics.ListAPIView):         #read
    queryset = doto.objects.all()
    serializer_class = dotoserializers

class dotoUpdateView(generics.UpdateAPIView):       #update
    queryset = doto.objects.all()
    serializer_class = dotoserializers
          



class dotoCreateView(generics.CreateAPIView):      #create
    serializer_class = dotoserializers
    queryset = doto.objects.all()   

class dotoDeleteView(generics.DestroyAPIView):  
    queryset = doto.objects.all()
    serializer_class = dotoserializers  

    



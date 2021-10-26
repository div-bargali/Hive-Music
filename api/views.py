from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.CreateAPIView):
    """
    View for creating room using serializer class
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import  Owner, Car, Message
from .serializers import OwnerSerializer, CarSerializer, MessageSerializer
from rest_framework.renderers import JSONRenderer


class OwnerCreateView(generics.CreateAPIView):
    serializer_class = OwnerSerializer


class OwnersListView(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarSerializer


class CarsListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer


class MessagesListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self, request, reg_number):
        try:
            return Message.objects.filter(sender=self.request.owner.tel_number, recipient=self.kwargs['reg_number']).reverse()
        except Exception as e:
            return None
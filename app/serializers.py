from rest_framework import serializers
from .models import Owner, Car, Message


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('tel_number', 'name')

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('reg_number', 'owners')


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'text', 'createdAt', 'received', 'read')
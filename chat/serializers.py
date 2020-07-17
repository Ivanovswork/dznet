from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Message


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Message


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class MessageSerializer(ModelSerializer):

    def to_representation(self, instance):
        result = super().to_representation(instance)

        if instance.sender.first_name or instance.sender.last_name:
            sender_name = instance.sender.get_full_name()
        else:
            sender_name = instance.sender.username

        if instance.receiver.first_name or instance.receiver.last_name:
            receiver_name = instance.receiver.get_full_name()
        else:
            receiver_name = instance.receiver.username

        result['sender_name'] = sender_name
        result['receiver_name'] = receiver_name
        return result

    class Meta:
        model = Message
        fields = '__all__'

# chat/serializers.py
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()

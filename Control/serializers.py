# chat/serializers.py
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(help_text="Mijoz murojaati")

    class Meta:
        swagger_schema_fields = {
            "example": {
                "text": "Salom, \"Energy Gym\" zali haqida ma'lumot ber!"
            }
        }

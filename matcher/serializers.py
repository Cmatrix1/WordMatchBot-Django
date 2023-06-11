from rest_framework import serializers
from .models import Condition, MessageResponse


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class MessageResponseSerializer(serializers.ModelSerializer):
    condition = serializers.StringRelatedField()

    class Meta:
        model = MessageResponse
        fields = ('id', 'response', 'condition')

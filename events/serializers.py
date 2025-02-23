from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user  
        return super().create(validated_data)

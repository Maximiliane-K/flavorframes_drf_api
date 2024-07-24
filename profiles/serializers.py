from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    location = serializers.CharField()


    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'screenname', 'city', 'location', 'about', 'profile_picture']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

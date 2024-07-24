from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    location = serializers.CharField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user == obj.owner
        return False

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'screenname', 'city', 'location', 'about', 'profile_picture', 'is_owner']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

from rest_framework import serializers
from .models import Follow
from django.contrib.auth.models import User

class FollowSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follow model.
    Adds extra fields to display the follower and following users.
    """

    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'followed_at']

    def validate(self, data):
        request = self.context.get('request')
        if request and request.user == data.get('following'):
            raise serializers.ValidationError("You cannot follow yourself.")
        return data

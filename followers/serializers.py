from rest_framework import serializers
from .models import Follow
from django.contrib.auth.models import User

class FollowSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follow model.
    Adds extra fields to display the follower and following users.
    """

    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'followed_at']

    def validate(self, data):
        request = self.context.get('request')
        #Validation to check if user is trying to follow themselves
        if request and request.user == data.get('following'):
            raise serializers.ValidationError("You cannot follow yourself.")

        #Validation to check for duplicate follow relationships
        if Follow.objects.filter(follower=request.user, following=data.get('following')).exists:
            raise serializers.ValidationError("You already are following this user.")

        return data


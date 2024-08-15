from rest_framework import serializers
from .models import Profile
from followers.models import Follow

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    location = serializers.CharField()
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user == obj.owner
        return False

    def get_following_id(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            follow = Follow.objects.filter(follower=user, following=obj.owner).first()
            return follow.id if follow else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'screenname',
            'city', 'location', 'about', 'profile_picture', 'is_owner', 
            'following_id'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

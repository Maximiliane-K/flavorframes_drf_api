from rest_framework import serializers
from .models import Profile
from followers.models import Follow
from django.db.models import Count

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.IntegerField(read_only=True)
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)
    profile_image = serializers.ImageField(source="profile_picture", required=False)

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user == obj.owner
        return False

    def get_following_id(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            following = Follow.objects.filter(
                follower=request.user, 
                following=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'screenname',
            'city', 'about', 'profile_image', 'is_owner',
            'following_id', 'posts_count', 'followers_count', 'following_count'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

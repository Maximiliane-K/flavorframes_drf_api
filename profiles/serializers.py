from rest_framework import serializers
from .models import Profile
from followers.models import Follow
from events.models import Event

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.IntegerField(read_only=True)
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)
    profile_image = serializers.ImageField(
        source="profile_picture", required=False)
    events_count = serializers.IntegerField(read_only=True)

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
            'id',
            'owner', 
            'created_at', 
            'updated_at', 
            'city', 
            'about', 
            'profile_image', 
            'is_owner',
            'following_id', 
            'posts_count', 
            'followers_count', 
            'following_count',
            'events_count',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        events_count = Event.objects.filter(owner=instance.owner).count()
        representation['events_count'] = events_count

        return representation

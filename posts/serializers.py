from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.profile_picture.url")

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_image',
            'created_at',
            'updated_at',
            'content',
            'image',
            'location_link',
            'like_id',
            'comments_count',
            'likes_count'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def get_like_id(self, obj):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            like = Like.objects.filter(user=request.user, post=obj)
            return like.first().id if like.exists() else None
        return None

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px')
        return value

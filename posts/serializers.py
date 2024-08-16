from rest_framework import serializers
from .models import Post
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'updated_at', 'content', 'image', 'location_link', 'like_id']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def get_like_id(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            like = Like.objects.filter(user=request.user, post=obj).first()
            return like.id if like else None
        return None

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

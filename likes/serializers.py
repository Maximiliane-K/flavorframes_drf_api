from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    Ensures a user can only like a post once.
    """

    user = serializers.ReadOnlyField(source='user.username')
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['id', 'timestamp', 'user', 'post', 'like_id']

    def get_like_id(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            like = Like.objects.filter(user=request.user, post=obj.post).first()
            return like.id if like else None
        return None

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'error': 'Duplicate like detected'})

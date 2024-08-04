from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.profile_picture.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        return request and request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            "id", "owner", "is_owner", "profile_id", "profile_image", 
            "post", "created_at", "updated_at", "content",
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read-only field so that we don't have to set it on each update
    """
    post = serializers.ReadOnlyField(source="post.id")

from rest_framework import serializers
from .models import Bookmark
from posts.models import Post

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'post', 'created_at']

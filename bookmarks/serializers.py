from rest_framework import serializers
from .models import Bookmark
from posts.models import Post
from posts.serializers import PostSerializer

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model.
    Shows detailed information about the bookmarked post. 
    """
    post = PostSerializer()

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'post', 'created_at']

from rest_framework import generics, permissions, filters
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """
    List and create posts when logged in.
    To associate logged-in user with post, the perform_create method is used.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['comments_count', 'likes_count', 'liked_by__timestamp']
    search_fields = ['owner__username', 'content']

    def get_queryset(self):
        return Post.objects.annotate(
            comments_count=Count('comment', distinct=True),
            likes_count=Count('liked_by', distinct=True) 
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and edit post if you are the owner.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.annotate(
            comments_count=Count('comment', distinct=True),
            likes_count=Count('liked_by', distinct=True)  
        ).order_by('-created_at')

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post")
        instance.delete()

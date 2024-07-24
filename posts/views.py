from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """
    List and create post when logged in.
    To associate logged in user with post the perform_create method is used.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and edit post if you are the owner.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post")
        instance.delete()

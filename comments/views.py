from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List and create comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a comment if you are the owner.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this comment")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment")
        instance.delete()

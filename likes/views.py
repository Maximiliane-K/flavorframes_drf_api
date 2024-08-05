from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from likes.models import Like
from likes.serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    List all likes and allow authenticated users to create new likes.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValidationError as e:
            raise ValidationError({"detail": "Duplicate like detected"})

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a like if you are the owner.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise ValidationError({"detail": "You do not have permission to delete this like"})
        instance.delete()

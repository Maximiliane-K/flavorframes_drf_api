from rest_framework import generics, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkListCreateView(generics.ListCreateAPIView):
    """
    View to list all bookmarks or create a new bookmark for the authenticated user.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetailView(generics.RetrieveDestroyAPIView):
    """
    View to retrieve or delete a bookmark.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

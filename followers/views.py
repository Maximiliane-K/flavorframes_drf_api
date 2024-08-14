from rest_framework import generics, permissions
from .models import Follow
from .serializers import FollowSerializer
from flavorframes_drf_api.permissions import IsOwnerOrReadOnly

class FollowList(generics.ListCreateAPIView):
    """
    List all follow relationships, i.e., all instances of users following others.
    Allow authenticated users to create a follow relationship.
    The perform_create function associates the current logged-in user as the follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a follow relationship.
    No update view since a user either follows or unfollows another user.
    The deletion is restricted to the owner of the follow relationship.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

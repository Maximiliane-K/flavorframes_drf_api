from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from flavorframes_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__user_followed_by', distinct=True),
        following_count=Count('owner__user_follows', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter, 
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__user_followed_by__following',
        'owner__user_follows__following',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__user_follows__followed_at',
        'owner__user_followed_by__followed_at',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__user_followed_by', distinct=True),
        following_count=Count('owner__user_follows', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

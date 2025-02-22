from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.response import Response
from flavorframes_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by Django signals.
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
        'owner__username',
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

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
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

    def update(self, request, *args, **kwargs):
        """
        Custom update method to ensure profile_picture is updated correctly.
        """
        print("Received FILES:", request.FILES)

        instance = self.get_object()
        data = request.data.copy()

        if "profile_picture" in request.FILES:
            instance.profile_picture = request.FILES["profile_picture"]

        response = super().update(request, *args, **kwargs)

        instance.city = data.get("city", instance.city)
        instance.about = data.get("about", instance.about)
        instance.save()

        return response

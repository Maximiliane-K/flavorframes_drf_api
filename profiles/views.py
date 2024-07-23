from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    Retrieve, update, or delete a profile if you are the owner.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        if profile.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

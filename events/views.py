from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from flavorframes_drf_api.permissions import IsOwnerOrReadOnly

class EventListView(generics.ListCreateAPIView):
    """
    List events or create an event if logged in.
    The perform_create method associates the event with the logged-in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all().order_by("-created_at")
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        "owner__profile": ["exact"],
        "category": ["exact"],
        "event_date": ["lte"],
    }
    search_fields = [
        "owner__username",
        "title",
        "event_date",
    ]
    ordering_fields = [
        "created_at",
        "event_date",
        "title",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all().order_by("-created_at")

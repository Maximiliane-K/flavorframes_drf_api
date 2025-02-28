from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Exists, OuterRef
from .models import Event
from .serializers import EventSerializer
from attendance.models import EventAttendance
from flavorframes_drf_api.permissions import IsOwnerOrReadOnly

class EventListView(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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

    def get_queryset(self):
        """
        Return all events and allow filtering for events the user is attending
        """
        queryset = Event.objects.all().order_by("-created_at")
        attending = self.request.query_params.get("attending", None)

        if attending and attending.lower() == "true" and self.request.user.is_authenticated:
            queryset = queryset.filter(
                Exists(
                    EventAttendance.objects.filter(
                        event=OuterRef("id"),
                        user=self.request.user,
                        status="attending",
                    )
                )
            )

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all().order_by("-created_at")

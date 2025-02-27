from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import EventAttendance
from .serializers import EventAttendanceSerializer
from events.models import Event

class EventAttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = EventAttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EventAttendance.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Fetch all users attending or interested in an event
        """
        event_id = request.query_params.get("event", None)
        if event_id:
            event = get_object_or_404(Event, id=event_id)
            attendees = EventAttendance.objects.filter(event=event)

            return Response({
                "attending": EventAttendanceSerializer(
                    attendees.filter(status="attending"), many=True
                ).data,
                "interested": EventAttendanceSerializer(
                    attendees.filter(status="interested"), many=True
                ).data,
            })
        return super().list(request, *args, **kwargs)

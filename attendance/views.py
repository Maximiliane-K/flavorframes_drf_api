from rest_framework import viewsets, permissions, status
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
                "attending_count": attendees.filter(status="attending").count(),
                "interested_count": attendees.filter(status="interested").count(),
                "attending": [
                    {
                        "id": a.id,
                        "user": a.user.username,
                        "profile_image": (
                            a.user.profile.profile_picture.url
                            if hasattr(a.user, 'profile') and a.user.profile.profile_picture
                            else None
                        ),
                    }
                    for a in attendees.filter(status="attending")
                ],
                "interested": [
                    {
                        "id": i.id,
                        "user": i.user.username,
                        "profile_image": (
                            i.user.profile.profile_picture.url
                            if hasattr(i.user, 'profile') and i.user.profile.profile_picture
                            else None
                        ),
                    }
                    for i in attendees.filter(status="interested")
                ],
            })
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Handle event attendance creation and return updated count
        """
        event_id = request.data.get("event")
        status_value = request.data.get("status")

        event = get_object_or_404(Event, id=event_id)

        attendance, created = EventAttendance.objects.get_or_create(
            user=request.user, event=event, defaults={"status": status_value}
        )

        if not created:
            attendance.status = status_value
            attendance.save()

        return Response({
            "attending_count": EventAttendance.objects.filter(event=event, status="attending").count(),
            "interested_count": EventAttendance.objects.filter(event=event, status="interested").count(),
            "status": attendance.status,
        }, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Handle event attendance removal using user & event ID instead of attendance ID
        """
        event_id = kwargs.get("pk")
        event = get_object_or_404(Event, id=event_id)

        attendance = EventAttendance.objects.filter(user=request.user, event=event).first()

        if attendance:
            attendance.delete()

        return Response({
            "attending_count": EventAttendance.objects.filter(event=event, status="attending").count(),
            "interested_count": EventAttendance.objects.filter(event=event, status="interested").count(),
            "status": None,
        }, status=status.HTTP_200_OK)


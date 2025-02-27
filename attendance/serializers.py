from rest_framework import serializers
from .models import EventAttendance

class EventAttendanceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    profile_image = serializers.ReadOnlyField(source="user.profile.profile_picture.url")

    class Meta:
        model = EventAttendance
        fields = ["id", "user", "profile_image", "event", "status"]

from rest_framework import serializers
from .models import Event
from attendance.models import EventAttendance

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.profile_picture.url"
    )
    user_status = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096px!")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096px!")
        return value

    def get_is_owner(self, obj):
        request = self.context.get("request")
        return request.user == obj.owner

    def get_user_status(self, obj):
        """
        Check if the current user is attending/interested in the event.
        """
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            attendance = EventAttendance.objects.filter(user=request.user, event=obj).first()
            return attendance.status if attendance else None
        return None

    class Meta:
        model = Event
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "description",
            "event_date",
            "category",
            "image",
            "user_status",
        ]

from django.db import models
from django.contrib.auth.models import User

class EventAttendance(models.Model):
    STATUS_CHOICES = [
        ("attending", "Attending"),
        ("interested", "Interested"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user} - {self.event} ({self.status})"



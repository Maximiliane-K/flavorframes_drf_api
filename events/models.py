from django.db import models
from django.contrib.auth.models import User

EVENT_CATEGORIES = (
    ("Food event", "Food event"),
    ("Drinks event", "Drinks event"),
    ("Sommerfestival", "Sommerfestival"),
    ("Winterfestival", "Winterfestival"),
    ("Exhibition", "Exhibition"),
    ("Other", "Other"),
)


class Event(models.Model):
    """
    Event model for users to create events
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default="Food event"
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} - {self.title}"

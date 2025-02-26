from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Post(models.Model):
    """
    Post model to store user posts with an Google Maps location link
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', 
        default='images/default_post_u8igak', 
        blank=True
    )
    location_link = models.URLField(
        max_length=200, 
        blank=True, 
        help_text="Enter the Google Maps link of the restaurant"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.owner.username}'

    def clean(self):
        """
        Validation for the location_link field to ensure it's a Google Maps link
        """
        if self.location_link and "google.com/maps" not in self.location_link:
            raise ValidationError({
                "location_link": "Please enter a valid Google Maps link"
            })
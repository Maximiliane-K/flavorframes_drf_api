from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ne57tp', blank=True
    )
    location_link = models.URLField(max_length=200, blank=True, help_text="Enter the Google Maps link of the restaurant")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.owner.username}'
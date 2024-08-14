from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
    """
    Follow model, tracks the relationship between users.
    'follower' is the User who is following another user.
    'following' is the User who is being followed.
    'unique_together' ensures that a user cannot follow another user more than once.
    """
    follower = models.ForeignKey(
        User, related_name='user_follows', on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name='user_followed_by', on_delete=models.CASCADE
    )
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-followed_at']
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'

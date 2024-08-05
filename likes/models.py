from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    """
    Represents a like on a post by a user.
    Each user can like a specific post only once.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='liked_by', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_user_post_like')
        ]

    def __str__(self):
        return f'Like by {self.user.username} on {self.post.id}'

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Bookmark(models.Model):
    """
    Model representing a bookmark for a post by a owner.
    """
    owner = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='bookmarked_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['owner', 'post'], name='unique_owner_post_bookmark')
        ]

    def __str__(self):
        return f"{self.owner.username} bookmarked {self.post.id}"

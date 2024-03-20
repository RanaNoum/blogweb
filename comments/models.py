# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Assuming user authentication

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # If using user authentication
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Optional: For moderation

    def __str__(self):
        return f"{self.content[:25]}..."

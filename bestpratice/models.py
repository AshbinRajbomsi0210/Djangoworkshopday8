from django.db import models
from django.contrib.auth.models import User

class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment on {self.post.title} by {self.created_at}'

class BlogPost(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
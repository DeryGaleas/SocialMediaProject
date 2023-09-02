from django.db import models

from User.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    title = models.CharField(max_length=280)
    content = models.CharField(max_length=500)
    post_image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    post_id = models.ForeignKey(Post, related_name="like", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

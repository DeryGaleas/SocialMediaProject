from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.CharField(max_length=300, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


class Friendship(models.Model):
    user_id = models.ForeignKey(User, related_name="friend_request_sent", on_delete=models.CASCADE)
    friend_id = models.ForeignKey(User, related_name="friend_request_received", on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('a', 'Accepted'),
        ('p', 'Pending'),
        ('r', 'Rejected')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='p')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


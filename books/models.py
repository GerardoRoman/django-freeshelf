from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=100)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resource(models.Model):
    MEDIA_TYPES = (
        ('article', 'Article'),
        ('book', 'Book'),
        ('website', 'Website'),
        ('video', 'Video'),
        ('other', 'Other'),
        # (what's in DB, what user sees)
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    media_type = models.CharField(choices=MEDIA_TYPES, max_length=50)
    url = models.URLField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=100)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resource(models.Model):
    # MEDIA_TYPES = (
    #     ('book', 'book'),
    #     ('webite', 'website')
    #     ('video', 'video')
    #     ('other', other)
    # )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    # media_type = ????
    url = models.URLField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

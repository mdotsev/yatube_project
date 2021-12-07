from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    text = models.TextField()
    slug = models.SlugField()
    description = models.TextField()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )

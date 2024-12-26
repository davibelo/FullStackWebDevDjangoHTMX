from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


class UserProfile(AbstractUser):
    pass


class Article(models.model):
    title = models.CharField(max_length=100)
    content = models.TextField(black=True, default="")
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default=ARTICLE_STATUS[0][0],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
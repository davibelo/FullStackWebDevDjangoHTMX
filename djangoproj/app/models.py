import re
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


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True)
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default=ARTICLE_STATUS[0][0],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def save(self, *args, **kwargs):  
    text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", "")
    self.word_count = len(re.findall(r"\b\w+\b", text))
    # super() is used to call the parent class method
    super().save(*args, **kwargs)
    
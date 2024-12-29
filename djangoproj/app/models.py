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
    word_count = models.IntegerField(blank=True, default=0)  # Set default value to 0
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default=ARTICLE_STATUS[0][0],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):  
        # Remove all HTML tags from the content using a regex pattern.
        # The pattern "<[^>]*>" matches any substring that starts with "<",
        # followed by zero or more characters that are not ">", and ends with ">".
        # This ensures that all HTML tags (e.g., <p>, <div>, <br>) are removed from the text.
        text = re.sub(r"<[^>]*>", "", self.content)

        # Replace any occurrences of the HTML non-breaking space (&nbsp;) with an empty string.
        # This ensures that these special HTML entities are removed from the text.
        text = text.replace("&nbsp;", "")

        # Calculate the word count by finding all word-like sequences in the cleaned text.
        # The regex pattern "\b\w+\b" matches:
        # - "\b": A word boundary, ensuring we start at the beginning of a word.
        # - "\w+": One or more alphanumeric characters (letters, digits, or underscores).
        # - "\b": Another word boundary, ensuring we end at the end of the word.
        # This ensures only valid words are counted, ignoring spaces, punctuation, or HTML artifacts.
        self.word_count = len(re.findall(r"\b\w+\b", text))

        # Call the parent class's save method to preserve its functionality.
        # This ensures that any additional processing defined in the parent class
        # is also executed when saving the object.
        super().save(*args, **kwargs)



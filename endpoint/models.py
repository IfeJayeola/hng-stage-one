from django.db import models

# Create your models here.

class PropertyModel(models.Model):
    length = models.IntegerField()
    is_palindrome = models.BooleanField()
    unique_characters = models.IntegerField()
    word_count = models.IntegerField()
    sha256_hash = models.CharField(max_length=64)
    character_frequency_map = models.JSONField()

class StringModel(models.Model):
    id = models.CharField(
        max_length=64,
        primary_key=True,
        editable=False
    )
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    property = models.OneToOneField(
        PropertyModel,
        on_delete=models.CASCADE,
    )

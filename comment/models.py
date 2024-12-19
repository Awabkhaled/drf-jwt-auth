from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):
    """Comments table with text and user only"""
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

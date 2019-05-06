from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class ReviewInput(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

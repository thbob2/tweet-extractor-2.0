from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField()
    user_name = models.CharField(max_length=50)
    user_handle = models.CharField(max_length=50)

    def __str__(self):
        return self.text
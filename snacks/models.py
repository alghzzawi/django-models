from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Thing(models.Model):
    name=models.CharField(max_length=64, help_text="the thing", default="thing")
    purchaser=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    descroption=models.TextField(default='descroption')

    def __str__(self):
        return self.name
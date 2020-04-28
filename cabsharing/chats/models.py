from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    writer=models.CharField(max_length=70)
    writer_photo=models.ImageField()
    message=models.CharField(max_length=500)
    time=models.TimeField(default=timezone.now)
# Create your models here.

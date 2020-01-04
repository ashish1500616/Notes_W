from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title=models.CharField((""), max_length=200,)
    text=models.TextField((""))
    date=models.DateTimeField(
            default=timezone.now)
    tag=models.ForeignKey('Tag', on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag=models.CharField((""), max_length=20,blank=False)
    def __str__(self):
        return self.tag

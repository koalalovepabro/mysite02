from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    hit = models.IntegerField(default=0)
    contents = models.CharField(max_length=2000)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

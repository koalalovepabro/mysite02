from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return "User(%s, %s, %s)" % (self.name, self.email, self.gender)


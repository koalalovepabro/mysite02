from django.db import models

# Create your models here.


class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    message = models.CharField(max_length=2000)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Guestbook(%s, %s, %s, %s)' % (self.name, self.password, self.message, str(self.regdate))


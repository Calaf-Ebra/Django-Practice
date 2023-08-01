from django.db import models

class DATA(models.Model):

    name = models.CharField(max_length=64)
    des = models.CharField(max_length=200)

    def __str__(self):
        return self.name + '  ' + self.des






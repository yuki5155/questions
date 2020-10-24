from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    food = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Convert(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, editable=False)
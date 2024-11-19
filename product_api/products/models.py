from django.db import models

# model here
class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
from django.db import models

class Menu(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField(max_length=6)
    bookingdate = models.DateTimeField()

    def __str__(self):
        return self.name
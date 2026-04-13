from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f'{self.title}:{self.price}'
    


class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateField(auto_now=False, default=None)

    def get_item(self):
        return f'{self.name}-{self.no_of_guests}-{self.booking_date}'
    
    def __str__(self):
        return f'{self.name}-{self.no_of_guests}-{self.booking_date}'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    #constructor 
    description = models.TextField(max_length=250)
    seat = models.CharField(max_length=100)
    price = models.IntegerField()
    event = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    # add the foreign key relating a ticket to customer
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    date = models.DateTimeField('event date and time')
    ageRestrict = models.IntegerField()
    ticketCount = models.IntegerField()
    availability = models.IntegerField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)



class Business(models.Model):
    name = models.CharField(max_length=100)
    # admins = models.What()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    # add the foreign key relating a ticket to customer
    user = models.ForeignKey(User, on_delete=models.CASCADE)
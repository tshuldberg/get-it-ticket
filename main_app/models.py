from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=100)
    # add the foreign key relating a ticket to customer
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business_detail', kwargs={'business_id': self.id})


class Venue(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business_detail', kwargs={'venue_id': self.id, 'business_id': self.business.id})


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField('event date and time')
    description = models.TextField(max_length=250)
    ageRestrict = models.IntegerField()
    ticketCount = models.IntegerField()
    availability = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_id': self.id, 'venue_id': self.venue.id, 'business_id': self.business.id})


class Ticket(models.Model):
    seat = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    # add the foreign key relating a ticket to customer
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# event = models.ForeignKey(Event, on_delete=models.CASCADE)
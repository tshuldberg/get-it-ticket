from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    # add the foreign key relating a ticket to customer
    user = models.ForeignKey(User, on_delete=models.CASCADE)
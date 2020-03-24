from django.forms import ModelForm
from .models import Event, Ticket

# class EventForm(ModelForm):
#   class Meta:
#     model = Event
#     fields = ['name', 'ageRestrict', 'ticketCount', 'date', 'availability', 'description']

# class TicketForm(ModelForm):
#   class Meta:
#     model = Ticket
#     fields = ['seat', 'price', 'category']
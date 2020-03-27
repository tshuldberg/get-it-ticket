from django.contrib import admin
from .models import Venue, Event, Business
# Register your models here.
admin.site.register(Venue)
admin.site.register(Business)
admin.site.register(Event)

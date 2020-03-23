from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Ticket, Venue, Event
from .forms import EventForm, TicketForm


# Create your views here.

class VenueCreate(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'event']

    def form_valid(self, form):
        # Assign the logged in user to the cat being created
        form.instance.user = self.request.user
        # Let CreateView's form_valid method do its thing
        return super().form_valid(form)

class VenueUpdate(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = 'event'

class VenueDelete(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/venue/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def venue_index(request):
    venue = Venue.objects.filter(user = request.user)
    return render(request, 'venue/index.html', {'venue': venue})

@login_required
def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)


    return render(request, 'venue/detail.html', {
        'venue': venue, 
        # 'event': eventdetails or all future events
    })

@login_required
def add_event(request, venue_id):
    form = EventForm(request.POST)

    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.venue_id = venue_id
        new_event.save()
    return redirect('detail', venue_id=venue_id)

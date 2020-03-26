from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Ticket, Venue, Event, Business
from .forms import EventForm, TicketForm, VenueForm

# # Create your views here.
def index(request):
    return render(request,'home.html')

def signup(request):
    error_message =''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid sign up - try again'"
    form = UserCreationForm()
    context = {'form': form, 'error_message' : error_message}
    return render(request, 'registration/signup.html', context)

# BUSINESS VIEW------------------------------------------------------------------------------
class BusinessCreate(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BusinessDelete(LoginRequiredMixin, DeleteView):
    model = Business
    success_url = '/business/'

@login_required
def business_detail(request, business_id):
    business = Business.objects.get(id=business_id)
    venue_form = VenueForm()
    return render(request, 'business/detail.html', {
        'business': business
    })

# VENUE VIEW---------------------------------------------------------------------------------
class VenueCreate(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'capacity']
    success_url = '/'
    def form_valid(self, form):
        # business_id = self.kwargs['business_id']
        form.instance.business = Business.objects.get(id=self.kwargs['business_id'])
        return super(VenueCreate, self).form_valid(form)

    def get_success_url(self, form):
        form.instance.business = Business.objects.get(id=self.kwargs['business_id'])
        return reverse('/business/', kwargs={'business_id', self.business_id})

class VenueDelete(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/business/'

@login_required
def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)

    return render(request, 'venue/detail.html', {
        'venue': venue, 
        # 'event': eventdetails or all future events
    })

# EVENT VIEWS---------------------------------------------------------------------------------
class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'date', 'description', 'ageRestrict', 'ticketCount', 'availability']

    def form_valid(self, form):
        # Assign the current venue to the event being created
        form.instance.venue = self.request.venue
        # Let CreateView's form_valid method do its thing
        return super().form_valid(form)

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'date', 'description', 'ageRestrict', 'ticketCount', 'availability']

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/venue/events'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def venue_index(request):
    venue = Venue.objects.filter(user = request.user)
    return render(request, 'venue/index.html', {'venue': venue})

@login_required
def add_event(request, venue_id):
    form = EventForm(request.POST)

    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.venue_id = venue_id
        new_event.save()
    return redirect('detail', venue_id=venue_id)
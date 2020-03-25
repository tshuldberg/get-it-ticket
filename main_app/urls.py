from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    #venue
    path('venue/', views.venue_index, name='index'),
    path('venue/<int:venue:id>/', views.venue_detail, name='detail'),
    path('venue/create/', views.VenueCreate.as_view(), name='venue_create'),
    path('venue/<int:pk>/update/', views.VenueUpdate.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete/', views.VenueDelete.as_view(), name='venue_delete'),
    #event
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('event/create/', views.EventCreate.as_view(), name='event_create'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),

]

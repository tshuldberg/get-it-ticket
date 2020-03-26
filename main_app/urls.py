from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    #venue
    # path('venue/', views.venue_index, name='venue_index'),
    path('business/', views.BusinessCreate.as_view(), name='business_create'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    path('venue/<int:venue:id>/', views.venue_detail, name='venue_detail'),
    path('venue/create/<int:business_id>/', views.VenueCreate.as_view(), name='venue_create'),
    path('venue/<int:pk>/update/', views.VenueUpdate.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete/', views.VenueDelete.as_view(), name='venue_delete'),
    #event
    
    # path('event/create/', views.EventCreate.as_view(), name='event_create'),
    # path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    # path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]

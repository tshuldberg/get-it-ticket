from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('venue/', views.venue_index, name='index'),
    path('venue/<int:venue:id>/', views.venue_detail, name='detail'),
    path('venue/create/', views.VenueCreate.as_view(), name='venue_create'),
    path('venue/<int:pk>/update/', views.VenueUpdate.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete/', views.VenueDelete.as_view(), name='venue_delete')
]

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    #venue
    # path('venue/', views.venue_index, name='venue_index'),
    path('user/<int:user_id>/businesses/', views.user_show_busnisses, name='business_admin'),
    path('business/', views.BusinessCreate.as_view(), name='business_create'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    # path('venue/<int:venue:id>/', views.venue_detail, name='venue_detail'),
    path('venue/create/<int:business_id>/', views.VenueCreate.as_view(), name='venue_create'),

    path('business/<int:business_id>/venue/<int:venue_id>/delete/', views.venue_delete, name='venue_delete'),
    path('business/<int:business_id>/venue/<int:venue_id>/', views.venue_detail, name='venue_detail'),
    #event
    path('business/<int:business_id>/venue/<int:venue_id>/event/create/', views.EventCreate.as_view(), name='event_create'),
    # path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    # path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]


#   <li><a href="{% url 'toys_index' %}">View All Toys</a></li>

#   path('toys/', views.ToyList.as_view(), name='toys_index'),

#              class ToyList(LoginRequiredMixin, ListView):
 #                   model = Toy

#  {% extends 'base.html' %}
# {% block content %}

# <h1>Toy List</h1>
# {% for toy in toy_list %}
#   <a href="{% url 'toys_detail' toy.id %}">
#     <div class="card">
#         <div class="card-content">
#             <span class="card-title">{{ toy.name }}</span>
#             <p>Color: {{ toy.color }}</p>
#         </div>
#     </div>
#   </a>
# {% endfor %}

# {% endblock %}


#   path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),

# class ToyDetail(LoginRequiredMixin, DetailView):
#   model = Toy
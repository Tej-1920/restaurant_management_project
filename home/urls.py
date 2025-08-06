from django.urls import path
from .views import *

urlpatterns = [
    path('api/restaurant/',RestaurantSerializerView.as_view(),name='restaurant-detail'),
]
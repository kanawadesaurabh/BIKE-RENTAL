from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path(
    "bike-search/",
    views.bike_search,
    name="bike_search"
),
]
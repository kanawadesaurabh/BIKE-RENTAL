from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('add/', views.add_bike, name='add_bike'),
    path('edit/<int:id>/', views.edit_bike, name='edit_bike'),
    path('delete/<int:id>/', views.delete_bike, name='delete_bike'),
]
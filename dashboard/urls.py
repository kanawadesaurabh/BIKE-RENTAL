from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path(
        "bike-search/",
        views.bike_search,
        name="bike_search"
    ),

    path(
        "export-excel/",
        views.export_excel,
        name="export_excel"
    ),
]
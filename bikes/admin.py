from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):

    list_display = (
        'bike_name',
        'brand',
        'registration_number',
        'daily_rent',
        'status'
    )

    search_fields = (
        'bike_name',
        'registration_number',
        'brand'
    )

    list_filter = (
        'status',
        'brand'
    )
from django.urls import path
from . import views

urlpatterns = [
    path("", views.rental_list, name="rental_list"),
    path("add/", views.add_rental, name="add_rental"),
    path("return/<int:id>/", views.return_bike, name="return_bike"),
    path("detail/<int:id>/", views.rental_detail, name="rental_detail"),
    path("invoice/<int:id>/", views.print_invoice, name="print_invoice"),
    path("detail/<int:id>/", views.rental_detail, name="rental_detail"),
    path("invoice/<int:id>/", views.print_invoice, name="print_invoice"),
]
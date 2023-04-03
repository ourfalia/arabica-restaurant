from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [
    path('book/', views.reserve_table, name='book'),
    path('bookings/', views.my_reservation, name='bookings'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('cancel/<item_id>', views.cancel_item, name='cancel'),
    path('cancelation/', views.cancelation, name='cancelation'),
]

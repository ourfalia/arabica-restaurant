from django.contrib import admin
from django.urls import path, include
from arabicafood.views import get_home, go_to_menu, go_to_contact
from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home/', get_home, name='home'),
    path('reservation/', views.reserve_table, name='reservation'),
    path('menu/', go_to_menu, name='menu'),
    path('contact/', go_to_contact, name='contact'),
    path('bookings/', views.my_reservation, name='bookings'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('edit/<item_id>', views.edit_item, name='edit'),
]

from django.contrib import admin
from django.urls import path, include
from arabicafood.views import get_home, go_to_menu, go_to_contact, make_reservation
from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home', get_home, name='home'),
    path('reservation', make_reservation, name='reservation'),
    path('menu', go_to_menu, name='menu'),
    path('contact', go_to_contact, name='contact')
]

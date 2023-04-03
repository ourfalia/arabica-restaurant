from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('arabicafood.urls', namespace='home')),
    path('', include('arabicafood.urls', namespace='get_home')),
    path('', include('reservation.urls', namespace='book')),
    path('', include('reservation.urls', namespace='menu')),
    path('', include('reservation.urls', namespace='contact')),
    path('', include('reservation.urls', namespace='bookings')),
    path('', include('reservation.urls', namespace='confirmation')),
    path('', include('reservation.urls', namespace='edit')),
    path('', include('reservation.urls', namespace='cancel')),
    path('', include('reservation.urls', namespace='cancelation')),
    path('accounts/', include('allauth.urls')),
]


# path('menu/', go_to_menu, name='menu'),
# path('contact/', go_to_contact, name='contact'),
# path('bookings/', my_reservation, name='bookings'),
# path('confirmation/', confirmation, name='confirmation'),
# path('edit/<item_id>', edit_item, name='edit'),
# path('cancel/<item_id>', cancel_item, name='cancel'),
# path('cancelation/', cancelation, name='cancelation'),
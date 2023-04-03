from django.urls import path
from . import views


app_name = 'arabicafood'

urlpatterns = [
    path('', views.get_home, name='get_home'),
    path('home/', views.get_home, name='home'),
    path('menu/', views.go_to_menu, name='menu'),
    path('contact/', views.go_to_contact, name='contact'),
]

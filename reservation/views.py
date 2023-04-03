from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation
from .forms import ReserveTableForm
from reservation.models import Reservation

# Create your views here.

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

            return redirect(confirmation)
    reserve_form = ReserveTableForm()
    context = {'form': reserve_form}

    return render(request, 'reservation/reservation.html', context)

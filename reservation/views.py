from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation
from .forms import ReserveTableForm
from reservation.models import Reservation

# Create your views here.
# return redirect(confirmation)
# return redirect('confirmation')


# def reserve_table(request):
#     reserve_form = ReserveTableForm()

#     if request.method == 'POST':
#         reserve_form = ReserveTableForm(request.POST)

#         if reserve_form.is_valid():
#             reserve_form.save()

#             return redirect(confirmation)
#     reserve_form = ReserveTableForm()
#     context = {'form': reserve_form}

#     return render(request, '../templates/book.html', context)


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return render(request, '../templates/confirmation.html')
    reserve_form = ReserveTableForm()
    context = {'form': reserve_form}

    return render(request, '../templates/book.html', context)


def my_reservation(request):
    booking = Reservation.objects.all()
    context = {
        'booking': booking
        }
    return render(request, '../templates/my_reservation.html', context)


def confirmation(request):
    return render(request, '../templates/confirmation.html')


def edit_item(request, item_id):
    item = get_object_or_404(Reservation, id=item_id)
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST, instance=item)
        if reserve_form.is_valid():
            reserve_form.save()
            return render(request, '../templates/confirmation.html')
    reserve_form = ReserveTableForm(instance=item)
    context = {'form': reserve_form}
    return render(request, '../templates/edit_item.html', context)


def cancel_item(request, item_id):
    item = get_object_or_404(Reservation, id=item_id)
    item.delete()
    return render(request, '../templates/cancelation.html')


def cancelation(request):
    return render(request, '../templates/cancelation.html')

from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
# Create your views here.
from .models import Trip


def home(request):
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': Trip.objects.all()
    }
    return render(request, 'home.html', context=home_context)


def detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        return render(request, 'detail.html', {'trip': trip})
    except ObjectDoesNotExist as e:
        return render(request, '404.html')


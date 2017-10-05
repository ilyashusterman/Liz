from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from .forms import TripForm
from .models import Trip


def home(request):
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': Trip.objects.all(),
        'form': TripForm()
    }
    return render(request, 'home.html', context=home_context)


def detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        return render(request, 'detail.html', {'trip': trip})
    except ObjectDoesNotExist as e:
        return render(request, '404.html')


def add_trip(request):
    form = TripForm(request.POST)
    if form.is_valid():
        trip = Trip(name=form.cleaned_data['name'],
                    destination=form.cleaned_data['destination'],
                    stops=form.cleaned_data['stops'],
                    img_url=form.cleaned_data['img_url'],
                    )
        trip.save()
    return HttpResponseRedirect('/')

from django.contrib.auth.models import User
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
    form = TripForm(request.POST, request.FILES)
    if form.is_valid():
        trip = form.save(commit=False)
        trip.user = request.user
        trip.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    try:
        user = User.objects.get(username=username)
        trips = Trip.objects.filter(user=user)
        return render(request, 'profile.html', {'travels': trips,
                                                'username': username,
                                                'form': TripForm()
                                                })
    except ObjectDoesNotExist as e:
        return render(request, '404.html')
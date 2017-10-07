from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from .forms import TripForm, LoginForm
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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('User is not Active')
            else:
                print('Incorrect username and password')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

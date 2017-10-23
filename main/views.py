from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from .forms import TripForm, LoginForm, ImageForm
from .models import Trip, TripImage


def home(request):
    ImageFormSet = modelformset_factory(TripImage,
                                        form=ImageForm, extra=3)
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': Trip.objects.all(),
        'form': TripForm(),
        'formset': ImageFormSet(queryset=TripImage.objects.none()),
        'images': TripImage.objects.all()
    }
    return render(request, 'home.html', context=home_context)


def detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        return render(request, 'detail.html', {'trip': trip})
    except ObjectDoesNotExist as e:
        return render(request, '404.html')


def add_trip(request):
    ImageFormSet = modelformset_factory(TripImage,
                                        form=ImageForm, extra=3)
    # form = TripForm(request.POST, request.FILES)
    form = TripForm(request.POST)
    formset = ImageFormSet(request.POST, request.FILES,
                           queryset=TripImage.objects.none())
    # trip = None
    if form.is_valid() and formset.is_valid():
        print(form)
        trip = form.save(commit=False)
        trip.user = request.user
        trip.save()
        # if trip is not None:
        for form_image in formset.cleaned_data:
            if 'image' in form_image:
                image = form_image['image']
                photo = TripImage(trip=trip, image=image)
                photo.save()

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


def like_trip(request):
    trip_id = request.POST.get('trip_id', None)
    likes = 0
    if trip_id:
        trip = Trip.objects.get(id=int(trip_id))
        if trip is not None:
            likes = trip.likes + 1
            trip.likes = likes
            trip.save()
    return HttpResponse(likes)


def sales(request):
    return render(request, 'sales.html', {'sales': {}})
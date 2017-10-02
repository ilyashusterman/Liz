from django.shortcuts import render

# Create your views here.
from .models import Trip


def home(request):
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': Trip.objects.all()
    }
    return render(request, 'home.html', context=home_context)
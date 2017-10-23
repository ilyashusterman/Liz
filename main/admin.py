from django.contrib import admin

from .models import Trip, TripImage

admin.site.register(Trip)
# Register your models here.

class TripImageInline(admin.TabularInline):
    model = TripImage
    extra = 3

class TripAdmin(admin.ModelAdmin):
    inlines = [TripImageInline, ]


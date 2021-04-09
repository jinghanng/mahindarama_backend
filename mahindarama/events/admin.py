from django.contrib import admin
from .models import Sangha, Location, Category, Event_Creator, Event


@admin.register(Sangha)
class SanghaAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Event_Creator)
class Event_CreatorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date",)

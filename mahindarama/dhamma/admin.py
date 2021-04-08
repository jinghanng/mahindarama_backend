from django.contrib import admin
from .models import Dhamma, Sangha, Location, Category, MediaType, Language

@admin.register(Dhamma)
class DhammaAdmin(admin.ModelAdmin):
    list_display = ("title", "record_date",)

@admin.register(Sangha)
class SanghaAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(MediaType)
class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)

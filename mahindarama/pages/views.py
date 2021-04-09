from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

HOME_PAGE_MESSAGE = getattr(settings, "HOME_PAGE_MESSAGE", "Missing message")


def home_view(request):
    return HttpResponse(f"<h1>{HOME_PAGE_MESSAGE}</h1>")

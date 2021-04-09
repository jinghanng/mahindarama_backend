from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dhamma import views

urlpatterns = [
    path('', views.dhamma),
]
urlpatterns = format_suffix_patterns(urlpatterns)

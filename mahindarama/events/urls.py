from django.urls import path
from .views import (
    EventFilterView,
)

urlpatterns = [
    path('', EventFilterView.as_view(), name='event')
]

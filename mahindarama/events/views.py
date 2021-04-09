from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Event, Category, Location
from .serializers import EventSerializer
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


def is_valid_queryparam(param):
    return param != '' and param is not None


def general(request):
    qs = Event.objects.all()
    return qs


def filter(request):
    qs = Event.objects.all()
    # categories = Category.objects.all()
    # location = Location.objects.all()
    # from_date = request.GET.get('from_date')
    # to_date = request.GET.get('to_date')
    # title_query = request.GET.get('title')
    # category = request.GET.get('category')
    # location = request.GET.get('location')

    # if is_valid_queryparam(title_query):
    #     qs = qs.filter(title__icontains=title_query)

    # if is_valid_queryparam(category):
    #     qs = qs.filter(categories__name__icontains=category)

    # if is_valid_queryparam(location):
    #     qs = qs.filter(location__name__icontains=location)

    # if is_valid_queryparam(from_date):
    #     qs = qs.filter(start_date__gte=from_date)

    # if is_valid_queryparam(to_date):
    #     qs = qs.filter(start_date__lt=to_date)
    #     print(qs)

    return qs


# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 6
#     page_size_query_param = 'page_size'
#     max_page_size = 500


class CustomPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })


class EventFilterView(ListAPIView):
    serializer_class = EventSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = Event.objects.all()
        print(qs)
        return qs

        class Meta:
            ordering = ['-id']

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response({
    #         "has_more": True
    #     })

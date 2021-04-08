from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Dhamma, Sangha, Location, Category, MediaType, Language 
from .serializers import DhammaSerializer
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


def is_valid_queryparam(param):
    return param != '' and param is not None


def general(request):
    qs = Dhamma.objects.all()
    return qs


def filter(request):
    qs = Dhamma.objects.all()
    sanghas = Sangha.objects.all()
    categories = Category.objects.all()
    mediatypes = MediaType.objects.all()
    languages = Language.objects.all()

    title = request.GET.get('title')
    category = request.GET.get('category')
    sangha = request.GET.get('sangha')
    mediatype = request.GET.get('mediatype')
    language = request.GET.get('language')

    if is_valid_queryparam(title):
        qs = qs.filter(title__icontains=title)
    
    if is_valid_queryparam(category):
        qs = qs.filter(categories__name__icontains=category)

    if is_valid_queryparam(sangha):
        qs = qs.filter(sanghas__name__icontains=sangha)

    if is_valid_queryparam(mediatype):
        qs = qs.filter(mediatypes__name__icontains=mediatype)
    
    if is_valid_queryparam(language):
        qs = qs.filter(languages__name__icontains=language)
        print(qs)

    return qs


def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Dhamma.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Dhamma.objects.all().count():
        return False
    return True


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


class DhammaFilterView(ListAPIView):
    serializer_class = DhammaSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = general(self.request)
        print(qs)
        return qs

        class Meta:
            ordering = ['-id']
    
    def is_there_more_datas(self, request):
        offset = request.GET.get('offset')
        if int(offset) > self.get_queryset().count():
            return False
        return True

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "dhammas": serializer.data,
            "has_more": self.is_there_more_datas(request)
        })

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from utils.error_codes import ResponseCodes
from mahindarama import pagination
from utils.generic_json_creator import create_response
from .models import Dhamma, Sangha, Location, Category, MediaType, Language
from .serializers import DhammaSerializer


def is_valid_queryparam(param):
    return param != '' and param is not None


@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def dhamma(request):
    dhamma = Dhamma.objects.all().order_by('id')
    title = request.GET.get('title')
    sangha = request.GET.get('sangha')
    category = request.GET.get('category')
    mediatype = request.GET.get('mediatype')
    language = request.GET.get('language')

    if is_valid_queryparam(title):
        dhamma = dhamma.filter(title__icontains=title)
    if is_valid_queryparam(sangha):
        dhamma = dhamma.filter(sangha_name__name=sangha)
    if is_valid_queryparam(category):
        dhamma = dhamma.filter(categories__name=category)
    if is_valid_queryparam(mediatype):
        dhamma = dhamma.filter(media_type__name=mediatype)
    if is_valid_queryparam(language):
        dhamma = dhamma.filter(language__name=language)

    paginator = pagination.CustomPagination()
    dhamma = paginator.paginate_queryset(dhamma, request)
    serialized_dhamma = DhammaSerializer(instance=dhamma, many=True).data

    return JsonResponse(create_response(data=serialized_dhamma, paginator=paginator), safe=False)

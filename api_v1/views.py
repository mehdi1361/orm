from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from .seriailizers.base_serializer import DateSerializer
from rest_framework import status
from base.models import Country, City, Category
from api_v1.seriailizers.base_serializer import CountrySerializer, CitySerializer
from api_v1.seriailizers.base_serializer import CityCountrserializer, CategorySerializer
from base.models import Language
from api_v1.seriailizers.base_serializer import LanguageSerializer
from movie.models import Film
from api_v1.seriailizers.movie_serializer import FilmSerializer
from common.decorators import cache
from api_v1.seriailizers.base_serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from common.proxy.user import VerificationUser
from user.models import Verification
from django.contrib import auth
from rest_framework_jwt.settings import api_settings


@api_view()
def get_date(request):
    data = {'message': datetime.now()}
    serializer = DateSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def list_country(request):
    c = Country.objects.all()
    s = CountrySerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK,)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_country(request, pk):

    try:
        c = Country.objects.get(pk=pk)
        s = CountrySerializer(c)
        return Response(s.data, status=status.HTTP_200_OK,)

    except Country.DoesNotExist:
        return Response(status=404)


@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_city(request, pk):
    try:
        c = City.objects.get(pk=pk)
        s = CitySerializer(c)
        return Response(s.data, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response(status=404)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_city_country(request, country):
    try:
        c = City.objects.filter(country__country=country)
        s = CityCountrserializer(c, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response(status=404)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def list_category(request):
    c = Category.objects.all()
    s = CategorySerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK)
@api_view()
@cache(cache_time=1 * 3600 * 24)
def list_language(request):
    c = Language.objects.all()
    s = LanguageSerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_language(request, pk):
    try:
        c = Language.objects.get(pk=pk)
        s = LanguageSerializer(c)
        return Response(s.data, status=status.HTTP_200_OK)
    except Language.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
@cache(cache_time=1 * 3600 * 24)
def get_film(request, page):
    f = (page-1) * 30
    d = page * 30
    query_set = Film.objects.all()[f:d]
    s = FilmSerializer(query_set, many=True)
    return Response(s.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@cache(cache_time=1 * 3600 * 24)
def get_film_category(request, pk, page):
    f = (page - 1) * 30
    d = page * 30
    query_set = Film.objects.filter(filmcategory=pk)[f:d]
    if query_set.exists():
        s = FilmSerializer(query_set, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    else:
        return Response(status=404)


@api_view(['GET'])
@cache(cache_time=1 * 3600 * 24)
def get_film_actor(request, pk, page):

    f = (page-1) * 30
    d = page * 30
    query_set = Film.objects.filter(filmactor=pk)[f:d]
    if query_set.exists():
        s = FilmSerializer(query_set, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    else:
        return Response(status=404)


@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_top(request, top):
    query_set = Film.objects.order_by('-rental_rate')[0:top]
    s = FilmSerializer(query_set, many=True)
    return Response(s.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_data(request):
    quary_set = request.user
    s = UserSerializer(quary_set)
    return Response(s.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def log_in(request):
    data = JSONParser().parse(request)
    try:

        if len(data['id']) == 18:
            v = VerificationUser(**data)
            v.send()
            return Response(data, status=status.HTTP_200_OK)
        else:
            raise Exception("the lenth of id not equal 18")

    except Exception as e:
        return Response({'id': 404, 'massage': e.args[0]}, status=400)

@api_view()
@cache(cache_time=1 * 3600 * 24)
def get_top_category(request, category, top):

    query_set = Film.objects.filter(category__name=category).order_by('-rental_rate')[0:top]
    if query_set:
        s = FilmSerializer(query_set, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    else:
        return Response(status=404)

# @permission_classes([IsAuthenticated])
@csrf_exempt
@api_view(['POST'])
def login_verify(request):
    data = JSONParser().parse(request)

    try:
        if Verification.verify_test(**data):

            user = auth.authenticate(request, username=data["dev_id"], password=data["dev_id"])
            if user is not None:
                auth.login(request, user)
                return Response({'username': data["dev_id"], 'token': api_settings.JWT_ENCODE_HANDLER(api_settings.JWT_PAYLOAD_HANDLER(user))})

        else:
            raise Exception("the username or code is incorrect")

    except Exception as e:
        return Response({'id': 404, 'massage': e.args[0]}, status=400)

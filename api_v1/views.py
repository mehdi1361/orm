from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriailizers.base_serializer import DateSerializer
from rest_framework import status
from base.models import Country, City, Category
from api_v1.seriailizers.base_serializer import CountrySerializer, CitySerializer
from api_v1.seriailizers.base_serializer import CityCountrserializer, CategorySerializer
from base.models import Language
from api_v1.seriailizers.base_serializer import LanguageSerializer
from movie.models import Film
from api_v1.seriailizers.movie_serializer import FilmSerializer


@api_view()
def get_date(request):
    data = {'message': datetime.now()}
    serializer = DateSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def list_country(request):
    c = Country.objects.all()
    s = CountrySerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK,)

@api_view()
def get_country(request, pk):

    try:
        c = Country.objects.get(pk=pk)
        s = CountrySerializer(c)
        return Response(s.data, status=status.HTTP_200_OK,)

    except Country.DoesNotExist:
        return Response(status=404)

@api_view()
def get_city(request, pk):
    try:
        c = City.objects.get(pk=pk)
        s = CitySerializer(c)
        return Response(s.data, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response(status=404)

@api_view()
def get_city_country(request, country):
    try:
        c = City.objects.filter(country__country=country)
        s = CityCountrserializer(c, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response(status=404)

@api_view()
def list_category(request):
    c = Category.objects.all()
    s = CategorySerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK)

@api_view()
def list_language(request):
    c = Language.objects.all()
    s = LanguageSerializer(c, many=True)
    return Response(s.data, status=status.HTTP_200_OK)

@api_view()
def get_language(request, pk):
    try:
        c = Language.objects.get(pk=pk)
        s = LanguageSerializer(c)
        return Response(s.data, status=status.HTTP_200_OK)
    except Language.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def get_film(request, page):
    f = (page-1) * 30
    d = page * 30
    query_set = Film.objects.all()[f:d]
    s = FilmSerializer(query_set, many=True)
    return Response(s.data, status=status.HTTP_200_OK)


@api_view(['GET'])
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
def get_film_actor(request, pk, page):
    f = (page-1) * 30
    d = page * 30
    query_set = Film.objects.filter(filmactor=pk)[f:d]
    if query_set.exists():
        s = FilmSerializer(query_set, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    else:
        return Response(status=404)

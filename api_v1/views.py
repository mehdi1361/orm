from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriailizers.base_serializer import DateSerializer
from rest_framework import status
from base.models import Country, City
from api_v1.seriailizers.base_serializer import CountrySerializer, CitySerializer


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

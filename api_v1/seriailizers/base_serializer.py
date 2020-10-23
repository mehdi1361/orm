from rest_framework import serializers
from base.models import Country
from base.models import City

class DateSerializer(serializers.Serializer):
    message = serializers.DateTimeField()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city']

class CityCountrserializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city']

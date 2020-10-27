from rest_framework import serializers
from base.models import Country
from base.models import City, Category, Language


class DateSerializer(serializers.Serializer):
    message = serializers.DateTimeField()


class CountrySerializer(serializers.ModelSerializer):
    citys = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country', 'citys']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city']

class CityCountrserializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "name"]

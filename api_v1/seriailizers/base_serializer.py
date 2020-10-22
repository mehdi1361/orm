from rest_framework import serializers
from base.models import Country

class DateSerializer(serializers.Serializer):
    message = serializers.DateTimeField()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country']

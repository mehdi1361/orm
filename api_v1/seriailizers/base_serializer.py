from rest_framework import serializers
class DateSerializer(serializers.Serializer):
    massege = serializers.DateTimeField()

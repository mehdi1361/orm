from rest_framework import serializers
class DateSerializer(serializers.Serializer):
    message = serializers.DateTimeField()

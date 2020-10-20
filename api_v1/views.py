from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriailizers.base_serializer import DateSerializer
from rest_framework import status

@api_view()
def get_date(request):

    data = { 'message':datetime.now()}
    serializer = DateSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)
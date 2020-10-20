from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def get_date(request):
    return Response({'massege': datetime.now()})

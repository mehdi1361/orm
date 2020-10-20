from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view()
def get_date(request):
    return JsonResponse({'massege': datetime.now()})


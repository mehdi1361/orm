from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api_v2.seriailizer.base_serializer_v2 import CategorySerializer
from rest_framework import viewsets
from base.models import Category


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        quaryset = Category.objects.all()
        categort_serial = CategorySerializer(quaryset, many=True)
        return Response(categort_serial.data)

    def retrieve(self, request, pk):
        quaryset = Category.objects.all()
        quaryset_get = get_object_or_404(quaryset, pk=pk)
        category_serial = CategorySerializer(quaryset_get)
        return Response(category_serial.data)

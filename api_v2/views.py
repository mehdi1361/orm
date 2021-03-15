from api_v2.seriailizer.base_serializer_v2 import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import Category
from django.http import Http404
from rest_framework import status
from common.decorators import cache

class CategoryDetail(APIView):

    def get_object(self, pk, format=None):
        try:
            return Category.objects.get(pk=pk)

        except Category.DoesNotExist:
            raise Http404

    @cache(cache_time=1 * 3600 * 24)
    def get(self, request, pk, format=None):
        cat = self.get_object(pk)
        s = CategorySerializer(cat)
        return Response(s.data, status=status.HTTP_200_OK)

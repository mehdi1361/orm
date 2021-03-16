from django.urls import path
from api_v2 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

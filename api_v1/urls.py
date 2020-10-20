from django.urls import path
from api_v1 import views

urlpatterns = [
    path('api/', views.get_date)
]

from django.urls import path
from api_v1 import views

urlpatterns = [
    path('api/v1/date', views.get_date),
    path('api/v1/base/country{site_url}', views.list_country),
]

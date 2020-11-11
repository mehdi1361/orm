from django.urls import path
from api_v1 import views

urlpatterns = [
    path('date', views.get_date),
    path('base/country', views.list_country),
    path('base/country/<int:pk>', views.get_country),
    path('base/city/<int:pk>', views.get_city),
    path('base/cities/<slug:country>', views.get_city_country),
    path('base/category/', views.list_category),
    path('base/language', views.list_language),
    path('base/language/<int:pk>', views.get_language)
]

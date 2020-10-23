from django.urls import path
from api_v1 import views

urlpatterns = [
    path('api/v1/date', views.get_date),
    path('api/v1/base/country', views.list_country),
    path('api/v1/base/country/<int:pk>', views.get_country),
    path('api/v1/base/city/<int:pk>', views.get_city)

]

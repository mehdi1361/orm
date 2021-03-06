"""orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from server_side.views import index
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from api_v2.view_set import CategoryViewSet
from rest_framework.routers import DefaultRouter

# creating Router object
router = DefaultRouter()
# Regisiter CategoryViewset with Router
router.register('category_api', CategoryViewSet, basename="category")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_v1.urls')),
    path('', index),
    path('api/v1/', include('api_v1.urls')),
    path('login/', obtain_jwt_token),
    path('api-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api/v2/', include('api_v2.urls')),
    path('api_view_set/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

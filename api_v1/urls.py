from rest_framework.routers import DefaultRouter

from api_v1.views.cars import AutoViewSet

routers = DefaultRouter()
routers.register(r'cars', AutoViewSet, 'cars')

urlpatterns = routers.urls
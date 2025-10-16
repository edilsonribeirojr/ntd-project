from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetsViewSet

router = DefaultRouter()
router.register(r'planets', PlanetsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

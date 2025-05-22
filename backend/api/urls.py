from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TesteViewSet

router = DefaultRouter()
router.register(r'teste', TesteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
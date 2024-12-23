from django.urls import path
from .views import EquipmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'equipments', EquipmentViewSet)

urlpatterns = router.urls

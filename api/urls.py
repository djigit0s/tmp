from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, total_cost

router = DefaultRouter()
router.register('resources', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('total-cost/', total_cost, name='total_cost'),
]

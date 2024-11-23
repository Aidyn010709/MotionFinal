from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryViewSet, ProductModelViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet)
router.register('product', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

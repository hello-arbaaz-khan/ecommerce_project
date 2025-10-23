from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,OrderViewSet
router = DefaultRouter()
router.register(r'draz', ProductViewSet, basename='draz')
router.register('orders', OrderViewSet, basename='orders')
urlpatterns = router.urls

from rest_framework_nested import routers
from .views import CollectionViewSet, ProductViewSet, ReviewViewSet

router = routers.SimpleRouter()
router.register(r'collections', CollectionViewSet)

collection_router = routers.NestedSimpleRouter(router, r'collections', lookup='collection')
collection_router.register(r'products', ProductViewSet, basename='collection-products')

product_router = routers.NestedSimpleRouter(collection_router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + collection_router.urls + product_router.urls
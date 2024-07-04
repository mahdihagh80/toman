from django.urls import path
from .views import ImageUploadView, ImageDeleteRetrieveView, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = router.urls

urlpatterns += [
    path('image/', ImageUploadView.as_view()),
    path('image/<int:pk>/', ImageDeleteRetrieveView.as_view()),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter

from menu.views import CategoryViewSet, FoodListCreateAPIView, FoodRetrieveUpdateDestroyAPIView


router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')


app_name = "menu"

urlpatterns = [
    path('', include(router.urls)),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyAPIView.as_view()),
    path('food/', FoodListCreateAPIView.as_view()),
]
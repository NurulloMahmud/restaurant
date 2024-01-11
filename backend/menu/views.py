from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from menu.serializers import CategorySerializer, FoodListCreateSerializer, FoodRetrieveUpdateDestroySerializer
from menu.models import Category, Food



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FoodRetrieveUpdateDestroySerializer  # Different serializer for creation
        return super().get_serializer_class()


class FoodRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        food_instance = get_object_or_404(Food, pk=pk)
        serializer = FoodListCreateSerializer(data=food_instance)

        if serializer.is_valid():
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK
            )

        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        food_instance = get_object_or_404(Food, pk=pk)
        serializer = FoodListCreateSerializer(data=food_instance)

        if serializer.is_valid():
            if serializer.validated_data['available_qty'] < 0:
                return Response(
                    {
                        "success": False, 
                        "message": "Available quantity cannot be less than 0"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            data = {
                "success": True, 
                "message": "Updated the data successfully", 
                "data": serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)
        
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        food_instance = get_object_or_404(Food, pk=pk)
        serializer = FoodListCreateSerializer(data=food_instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {"success": True, 
                    "message": "Updated the data successfully", 
                    "data": serializer.data}

            return Response(data=data, status=status.HTTP_200_OK)
        
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        food_instance = get_object_or_404(Food, pk=pk)
        
        if food_instance is not None:
            food_instance.delete()

            data = {"success": True, 
                    "message": "Deleted the data successfully", 
                    "data": serializer.data}

            return Response(data=data, status=status.HTTP_200_OK)
        
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
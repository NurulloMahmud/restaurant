from rest_framework import serializers
from menu.models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodListCreateSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Food
        fields = '__all__'


class FoodRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), read_only=False, required=True
    )

    class Meta:
        model = Food
        fields = '__all__'


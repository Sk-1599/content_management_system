from rest_framework import serializers
from .models import User, ContentItem, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'

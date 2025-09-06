# import class serializers
from rest_framework.serializers import ModelSerializer

# import Category Model
from .models import Category

# Membuat class Serializers untuk API endpoint "Get list of categories"
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

# Membut class Serializers untuk API Endpoint "Get detail of category"
class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at',)

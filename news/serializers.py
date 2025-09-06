# import class serializers
from rest_framework.serializers import ModelSerializer
# import user model
from django.contrib.auth.models import User

# import Category Model dan lain nya
from .models import Category, News, Comment

# Membuat class Serializers untuk API endpoint "Get list of categories"
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

# Membuat class Serializers untuk API Endpoint "Get detail of category"
class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at',)

# Membuat class UserSerializer yang akan berelasi ke NewsSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'first_name', 'last_name',)

# Membuat class CommentFormSerializer yang akan berelasi ke NewsSerializer
class CommentFormSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)

class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields=('id', 'name', 'content', 'created_at',)

# Membuat class NewsListSerializer untuk API Endpoint "Get List of News"
class NewsListSerializer(ModelSerializer):
    user = UserSerializer(read_only=True) # Relasi ke modul / tabel user
    categories = CategoryListSerializer(many=True, read_only=True) # Relasi ke modul/tabel category

    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'user', 'categories', 'published_at')

# Membuat class NewsDetailSerializer untuk API Endpoint "Get Detail of News"
class NewsDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True) # relasi ke modul/tabel user
    categories = CategoryListSerializer(many=True, read_only=True) # relasi ke modul/tabel category
    comments = CommentListSerializer(many=True, read_only=True, source='comment_set') # relasi ke modul/tabel comment

    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'content', 'cover', 'published_at', 'user', 'categories', 'comments',)
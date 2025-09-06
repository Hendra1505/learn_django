# import class yang dibutuhkan untuk membuat view
from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Import Category Model dan class serializers untuk modul Category
from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer


# Create your views here.
# Membuat view untuk API Endpoint "Get All Categories"
# /api/category
class CategoryListView(ListAPIView):
    # mengeset class serializers
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    # Menambahkan fitur filtering, searching dan ordering
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    # mengeset fields/kolom untuk fitur filtering
    filter_fields=['name']
    # mengeset fields/kolom untuk fitur searching
    search_fields=['name']
    # mengeset fields/kolom untuk fitur ordering
    ordering_fields=['name', 'created_at']
    # mengeset fields/kolom default untuk fitur ordering
    ordering=['created_at']


# Membuat View untuk API Endpoint "Get Detail of Category"
# /api/category/:id
class CategoryDetailView(RetrieveAPIView):
    # mengeset class serializers
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from category import serializer
from .models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializer.CategoryListCategory
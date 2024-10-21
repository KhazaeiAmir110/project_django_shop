from rest_framework import viewsets

from apps.catalog.models import Category
from apps.catalog.serializers.admin import CreateCategoryNodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryNodeSerializer

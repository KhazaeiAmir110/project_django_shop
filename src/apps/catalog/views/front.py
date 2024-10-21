from rest_framework import viewsets

from apps.catalog.serializers.front import CategorySerializer
from apps.catalog.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer

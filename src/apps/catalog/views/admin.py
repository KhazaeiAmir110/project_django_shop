from rest_framework import viewsets

from apps.catalog.models import Category
from apps.catalog.serializers.admin import CreateCategoryNodeSerializer, CategoryTreeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryNodeSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryTreeSerializer
        else:
            return CreateCategoryNodeSerializer

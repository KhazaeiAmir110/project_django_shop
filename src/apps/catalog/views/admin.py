from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from apps.catalog.models import Category
from apps.catalog.serializers.admin import (
    CreateCategoryNodeSerializer, CategoryTreeSerializer, CategoryNodeSerializer, \
    CategoryModificationSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryNodeSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            case 'create':
                return CreateCategoryNodeSerializer
            case 'retrieve':
                return CategoryNodeSerializer
            case 'update' | 'partial_update' | 'destroy':
                return CategoryModificationSerializer
            case _:
                raise NotAcceptable()


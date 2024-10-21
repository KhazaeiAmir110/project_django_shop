from django.db import models

from treebeard.mp_tree import MP_Node

from apps.catalog.managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    public = models.BooleanField(default=False)
    slug = models.SlugField()

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

from django.db import models

from apps.catalog.models import Product


class StockRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_records')
    sku = models.CharField(max_length=50, null=True, blank=True)
    buy_price = models.PositiveIntegerField(null=True, blank=True)
    sell_price = models.PositiveIntegerField(null=True, blank=True)
    num_stock = models.PositiveIntegerField(null=True, blank=True)
    threshold_low_stake = models.PositiveIntegerField(null=True, blank=True)

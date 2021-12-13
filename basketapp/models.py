from django.db import models
from django.conf import settings
from mainapp.models import Product, ProductCategory
from django.utils.functional import cached_property


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

    @cached_property
    def get_item_cached(self):
        return self.user.basket.select_related()

    @property
    def product_cost(self):
        return self.quantity * self.product.price

    @property
    def total_quantity(self):
        _item = self.get_item_cached
        return sum(list(map(lambda x: x.quantity, _item)))

    @property
    def total_cost(self):
        _item = self.get_item_cached
        return sum(list(map(lambda x: x.product_cost, _item)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

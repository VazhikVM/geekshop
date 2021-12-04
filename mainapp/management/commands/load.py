import json
from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


def load_json_in_db(name_file):
    with open(f"{settings.BASE_DIR}/geekshop/json/{name_file}.json", 'r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_json_in_db('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_json_in_db('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            category_item = ProductCategory.objects.get(name=category_name)
            product['category'] = category_item
            Product.objects.create(**product)

    ShopUser.objects.create_superuser('django', password='geekbrains', age='31')


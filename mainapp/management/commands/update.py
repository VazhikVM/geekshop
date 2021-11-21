from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            ShopUserProfile.objects.create(user=user)

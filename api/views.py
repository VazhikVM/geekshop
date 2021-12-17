from mainapp.models import Product, ProductCategory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ProductSerializers, CategorySerializers


@api_view(['GET'])
def api_product(request):
    if request.method == 'GET':
        api_products = Product.objects.all()
        serializer = ProductSerializers(api_products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_category(request):
    if request.method == 'GET':
        api_categories = ProductCategory.objects.all()
        serializer = CategorySerializers(api_categories, many=True)
        return Response(serializer.data)

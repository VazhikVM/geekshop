import json
from geekshop import settings
from mainapp.models import Product, ProductCategory
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import ProductSerializers, CategorySerializers
from rest_framework.generics import CreateAPIView


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


class ApiProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # def create(self, request, *args, **kwargs):
    #     req_data = request.data.copy()
    #     with open(f'{settings.BASE_DIR}/geekshop/json/products.json') as f:
    #         templates = json.load(f)
    #     print(templates)
    #     requirements = req_data.pop(templates)
    #     serializers_data = []
    #     for requirement in requirements:
    #         req_data['requirement'] = requirement
    #         serializer = self.get_serializer(data=req_data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         serializers_data.append(serializer.data)
    #     return Response(serializers_data, status=status.HTTP_201_CREATED)

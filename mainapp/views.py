from django.http import request
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import random

# Create your views here.


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)[0]

def get_same_products(hot_product):
    product_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return product_list


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return None


def index(request):
    context = {
        'title': 'Главная',
        'Product': Product.objects.all()[:4],
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {
                'name': 'все',
                'pk': '0'}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)
        context = {
            'links_menu': ProductCategory.objects.all(),
            'title': 'Продукты',
            'category': category_item,
            'products': products_list,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', context=context)

    hot_product = get_hot_product()
    same_products = Product.objects.all()[3:6]

    context = {
        'links_menu': links_menu,
        'title': 'Продукты',
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user),

    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    link_menu = Product.objects.all()
    context = {
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'link_menu': link_menu,
    }
    return render(request, 'mainapp/product.html', context)
from django.http import request
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q


def get_product():
    if settings.LOW_CACHE:
        key = 'products'
        links_product = cache.get(key)

        if links_product is None:
            links_product = Product.objects.all()
            cache.set(key, links_product)
        return links_product
    return Product.objects.all()


def get_link_menu():
    if settings.LOW_CACHE:
        key = 'categories'
        links_menu = cache.get(key)

        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    return ProductCategory.objects.filter(is_active=True)


def get_hot_product():
    return random.sample(list(get_product()), 1)[0]


def get_same_products(hot_product):
    product_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk).select_related()[:3]
    return product_list


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return None


def index(request):
    context = {
        'title': 'Главная',
        'Product': Product.objects.filter(
            Q(category__name='дом') | Q(category__name='офис')
        ),
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None, page=1):
    links_menu = get_link_menu()
    if pk is not None:
        if pk == 0:
            products_list = get_product()
            category_item = {
                'name': 'все',
                'pk': '0'}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        paginator = Paginator(products_list, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
            'links_menu': get_link_menu(),
            'title': 'Продукты',
            'category': category_item,
            'products': products_paginator,
        }
        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_product()[3:6]

    context = {
        'links_menu': links_menu,
        'title': 'Продукты',
        'hot_product': hot_product,
        'same_products': same_products,

    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    link_menu = get_product()
    context = {
        'product': get_object_or_404(Product, pk=pk),
        'link_menu': link_menu,
    }
    return render(request, 'mainapp/product.html', context)

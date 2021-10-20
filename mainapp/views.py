from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'Главная',
        'Product': Product.objects.all()[:3],
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'Продукты',

    }
    return render(request, 'mainapp/products.html', context=context)

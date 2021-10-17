from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'title': 'Продукты'
    }
    return render(request, 'mainapp/products.html', context)


links_menu = [
    {
        'url': 'products',
        'title': 'все'
    },
    {
        'url': 'products_home',
        'title': 'дом'
    },
    {
        'url': 'products_office',
        'title': 'офис'
    },
    {
        'url': 'products_modern',
        'title': 'модерн'
    },
    {
        'url': 'products_classic',
        'title': 'классика'
    },
]


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'Дом'

    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'Офис'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'Модерн'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'Классика'
    }
    return render(request, 'mainapp/products.html', context=context)

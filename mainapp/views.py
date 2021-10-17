from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def contact(request):

    return render(request, 'mainapp/contact.html')


def products(request):
    return render(request, 'mainapp/products.html')


links_menu = [
    {'url': 'products',
     'title': 'Все'
     },
    {'url': 'products_home',
     'title': 'Дом'
     },
    {'url': 'products_office',
     'title': 'Офис'
     },
    {'url': 'products_modern',
     'title': 'Модерн'
     },
    {'url': 'products_classic',
     'title': 'Классика'
     }
]


def products_home(request):
    context = {
        'links_menu': links_menu

    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu': links_menu

    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu': links_menu

    }
    return render(request, 'mainapp/products.html', context=context)


def products_classic(request):
    context = {
        'links_menu': links_menu

    }
    return render(request, 'mainapp/products.html', context=context)

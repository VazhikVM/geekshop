from django.conf import settings
from django import template

register = template.Library()


@register.filter(name='media_for_products')
def media_for_products(path):
    if not path:
        path = 'produst/default.jpg'

    return f'{settings.MEDIA_URL}{path}'


@register.filter(name='media_for_users')
def media_for_users(path):
    if not path:
        path = 'user_avatar/default.jpg'

    return f'{settings.MEDIA_URL}{path}'

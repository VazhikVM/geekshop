from django.urls import path
from api import views as api

app_name = 'api'

urlpatterns = [
    path('product/', api.api_product, name='api_product'),
    path('category/', api.api_category, name='api_categories'),
    path('create/', api.ApiProductCreate.as_view(), name='create'),
]

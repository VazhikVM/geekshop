from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from django import forms

from mainapp.models import Product, ProductCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'
            fields.help_text = ''


class ProductCategoryEditForm(forms.ModelForm):
    discount = forms.IntegerField(label='Скидка', min_value=0, max_value=90, initial=0, required=False)


    class Meta:
        model = ProductCategory
        fields = '__all__'
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'
            fields.help_text = ''
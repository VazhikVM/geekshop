from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.db.models import F


class AccessMixin:
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'


class UserCreateView(AccessMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserRegisterForm

    def get_success_url(self):
        return reverse('adminapp:user_list')


class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserEditForm

    def get_success_url(self):
        return reverse('adminapp:user_list')


class UserDeleteView(AccessMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    form_class = ShopUserEditForm

    def get_success_url(self):
        return reverse('adminapp:user_list')


class CategoryCreateView(AccessMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('adminapp:category_list')


class CategoryListView(AccessMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'


class CategoryUpdateView(AccessMixin, UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_form.html'
    success_url = reverse_lazy('adminapp:category_list')

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data.get('discount')
            if discount:
                self.object.product_set.update(
                    price=F('price') * (1 - discount/100)
                )
        return super().form_valid(form)


class CategoryDeleteView(AccessMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('adminapp:category_list')


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     current_user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         if current_user.is_active:
#             current_user.is_active = False
#         else:
#             current_user.is_active = True
#         current_user.save()
#         return HttpResponseRedirect(reverse('adminapp:user_list'))
#
#     context = {
#         'object': current_user
#     }
#     return render(request, 'adminapp/user_delete.html', context)

class ProductCreateView(AccessMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        return reverse('adminapp:product_list', args=[self.kwargs['pk']])


class ProductsListView(AccessMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        return context_data

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))


class ProductsUpdateView(AccessMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])


class ProductDeleteView(AccessMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])


class ProductDetailView(AccessMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

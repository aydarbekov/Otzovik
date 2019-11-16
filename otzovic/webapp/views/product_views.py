from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    ordering = 'name'
    # paginate_by = 5
    # paginate_orphans = 1


class ProductView(DetailView):
    template_name = 'product/product.html'
    pk_url_kwarg = 'pk'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'obj'
    permission_required = 'webapp.change_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
    permission_denied_message = "Доступ запрещён"
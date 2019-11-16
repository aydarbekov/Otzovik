from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ProductReviewForm
from webapp.models import Product, Review


class ReviewForProductCreateView(CreateView):
    template_name = 'review/create.html'
    form_class = ProductReviewForm

    def form_valid(self, form):
        user = self.request.user
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        product.reviews.create(user=user, **form.cleaned_data)
        return redirect('webapp:product_view', pk=product_pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ProductReviewForm
    context_object_name = 'obj'
    permission_required = 'webapp.change_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})

class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'review/delete.html'
    model = Review
    context_object_name = 'obj'
    permission_required = 'webapp.delete_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})
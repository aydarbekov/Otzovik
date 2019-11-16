from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'picture']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'point']


from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
# Create your views here.


class CreateCategory(CreateView):
    template_name = "create_category.html"
    model = Category
    success_url = reverse_lazy("movies")


class CreateProduct(CreateView):
    template_name = "create_product.html"
    model = Product
    success_url = reverse_lazy("movies")

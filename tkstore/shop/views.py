from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
#from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
#from django.urls import reverse_lazy


# Create your views here.


def all_products(requests):
    products = Product.objects.all()
    return render(requests, 'home.html', {'products': products})


def product_detail(request):

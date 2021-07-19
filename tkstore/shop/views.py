from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


# Create your views here.
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def product_all(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'single.html', {'product': product})


def categories(request):
    return {
        'categories': Category.objects.all()
    }

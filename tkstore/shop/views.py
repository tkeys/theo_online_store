from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from .forms import ContactForm, SignUpForm


# Create your views here.
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


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    # success_url = reverse_lazy("movies")


class CreateCategory(CreateView):
    template_name = "create_category.html"
    model = Category
    fields = "__all__"
    permission_required = "viewer.add_movie"


class CreateProduct(CreateView):
    template_name = "create_product.html"
    model = Product
    fields = "__all__"
    permission_required = "viewer.add_movie"


class SignUpView(CreateView):
    template_name = "registration/create_account.html"
    form_class = SignUpForm


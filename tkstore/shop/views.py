from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product


# Create your views here.
def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is my first project</h1>")
    return render(request, "contact.html", {})


#def all_categories(request):
   # category = None
   # categories = Category.objects.all()
   # products = Product.objects.filter(available=True)
    # if category_slug:
    # category = get_object_or_404(Category, slug=category_slug)
    # products = products.filter(category=category)
    #return render(request, 'store.html', {'category': category,
                                        #  'categories': categories,
                                         # 'products': products})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# adding view to display single product
#def product_detail(request, slug):
    #product = get_object_or_404(Product, slug=slug, available=True)
    #cart_product_form = CartAddproductForm()
    #return render(request,
                  #'detail.html',
                  #{'product': product, 'cart_product_form': cart_product_form})

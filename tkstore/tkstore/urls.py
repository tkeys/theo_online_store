"""tkstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views
from shop.views import ContactView, CreateCategory, CreateProduct, SignUpView
from django.urls import include

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('basket/', include('basket.urls', namespace='basket')),
    path("shop/newcategory", CreateCategory.as_view(), name="create_category"),
    path("shop/newproduct", CreateProduct.as_view(), name="create_product"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

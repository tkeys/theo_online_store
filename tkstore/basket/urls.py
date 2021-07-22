from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [path('', views.basket_summary, name='basket_summary'),
               ]

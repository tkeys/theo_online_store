from django.contrib import admin
from .models import Category, Product


# Register your models here.
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    #prepopulated_fields = {'slug': ('name',)}


#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'created', 'updated']
    #prepopulated_fields = {'slug': ('name',)}

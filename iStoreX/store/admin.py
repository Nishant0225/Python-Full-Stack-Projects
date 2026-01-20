from django.contrib import admin
from .models import *
# Register your models here.
class CategoryClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description', 'image')

admin.site.register(CategoryModelClass, CategoryClassAdmin)
admin.site.register(ProductModelCLass, ProductClassAdmin)

from django.contrib import admin
from .models import *

@admin.register(Product)  
class Product (admin.ModelAdmin):
    pass

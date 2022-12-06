from django.contrib import admin
from.models import *
from django.contrib import admin
from .models import Products
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products)
admin.site.register(Cart)
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from user.models import Customer


# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return self.category

class SubCategory(models.Model):
    subCategory=models.CharField(max_length=100, verbose_name="Subcategory name")
    
    def __str__(self):
        return self.subCategory



class Products(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    subCategory = models.ManyToManyField(SubCategory, blank=True)
    name=models.CharField(max_length=100, verbose_name="Name")
    detail=models.TextField(max_length=600, verbose_name="Detail")
    price=models.IntegerField(verbose_name="Price")
    picture=models.FileField(upload_to='products/', null=True, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    piece = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return self.product.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
    
	def __str__(self):
		return str(self.id)
	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
    

class OrderItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
    
	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
       

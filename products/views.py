from django.shortcuts import render, redirect
from.models import *
from django.db.models import Q
from multiprocessing import context
from re import search
from.forms import *
from django.contrib import messages
# from .models import FeedFile


# Create your views here.
def index(request):
    products = Products.objects.all()
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    bottomPhotos = Products.objects.all().order_by('?')[:3]
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        products = Products.objects.filter(
            Q(name__icontains=search) | 
            Q(category__category__icontains=search) |
            Q(subCategory__subCategory__icontains=search) 
        ).distinct()
    context={
        'products' : products,
        'search' : search,
        'category' : category,
        'subCategory' : subCategory,
        'bottomPhotos':bottomPhotos
    }
    return render(request, 'index.html', context)

def contactUs(request):
    return render(request,'contactUs.html')



def productDelete(request, productId):
    urun = OrderItem.objects.get(id = productId)
    urun.delete()
    messages.success(request, 'The product has been deleted')
    return redirect('cart')

def myProduct(request):
    products = Products.objects.filter(creater = request.user)
    if request.method == "POST":
        delete = request.POST['delete']

        products = Products.objects.get(id = delete)
        products.delete()
        messages.success(request, "The product has been deleted")
        return redirect('myProduct')
    context={
        "products": products
    }
    return render(request,'myProduct.html', context)

def createProduct(request):
    form = ProductForm()
    user = request.user
        
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if user.is_superuser:
                user=form.save(commit=False)
                user.creater=request.user
                user.save()
                messages.success(request,"Product created!")
                return redirect("myProduct")
            else:
                messages.error(request, 'You are not authorized')
                return redirect('index')
    context = { 
        "form" : form 
    }   
    return render(request, "create.html", context) 

   
def productDetail(request, pk):
	product = Products.objects.get(id=pk)

	if request.method == 'POST':
		product = Products.objects.get(id=pk)
		#Get user account information
		try:
			customer = request.user.customer	
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
		orderItem.quantity=request.POST['quantity']
		orderItem.save()

		return redirect('cart')

	context = {'product':product}
	return render(request, 'productDetail.html', context)

def cart(request):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)
    

	context = {'order':order}
	return render(request, 'cart.html', context)
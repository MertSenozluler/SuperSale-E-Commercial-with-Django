"""supersale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from products.views import *
from django.conf.urls.static import static
from django.conf import settings
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contactUs/', contactUs, name='contactUs'),
    path('login/', userLogin, name='login'),
    path('register/', userRegister, name='register'),
    path('cart/',cart, name='cart'),
    path('logout/', userLogout, name='logout'),
    path('myProduct/', myProduct, name='myProduct'),
    path('create/', createProduct, name='create'),
    path('user/', user, name="user"),
    path('productDetail/<str:pk>/', productDetail, name="productDetail"),
    path('delete/<int:productId>', productDelete, name='delete')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

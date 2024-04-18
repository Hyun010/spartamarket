from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    products=Product.objects.all().order_by('-created_at')
    context={"products": products}
    return render(request,"products/products.html",context)

def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
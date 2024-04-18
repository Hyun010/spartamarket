from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from .forms import ProductForm
# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    products=Product.objects.all().order_by('-created_at')
    context={"products": products}
    return render(request,"products/products.html",context)

def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    context={"product": product}
    return render(request,"products/product_detail.html",context)

@login_required
def create(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            product=form.save(commit=False)
            product.author=request.user
            product.save()
            return redirect("products:product_detail",product.id)
    else:
        form=ProductForm()
    context={"form": form}
    return render(request,"products/create.html",context)
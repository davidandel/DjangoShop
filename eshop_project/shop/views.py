from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:8]  # zobrazíme jen prvních 8 produktů
    return render(request, 'shop/home.html', {'categories': categories, 'products': products})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

def products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def contact(request):
    return render(request, 'shop/contact.html')




def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})

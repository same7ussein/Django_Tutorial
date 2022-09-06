from django.shortcuts import render
from .models import Products

def product(request):
    return render(request,'product/product.html')

def products(request):
    product=Products.objects.all()
    all_products={'pro':product}
    #all_product={'pro':product.filter(price__exact=10)}
    #تعني عرض المنتجات الي سعرها يساوي عشره بالظبط
    #all_product={'pro':product.filter(name__contains='a')}
    #تعني عرض المنتجات الي تحتوي علي حرف ال a
    #all_product={'pro':product.filter(price__in=[10,100,500])}
    #عرض المنتجات الي سعرها 10, 100, 500

    #all_product={'pro':product.filter(price__range=(10,500))}
    #تعني عرض المنتجات الي سعرها يتراوح بين 10و500
    return render(request,'product/products.html',all_products)

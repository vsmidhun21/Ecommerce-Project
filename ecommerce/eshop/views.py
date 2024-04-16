from django.shortcuts import redirect, render
from .models import Category, Products
from django.contrib import messages

def home(request):
    return render(request,"shop/index.html")

def login(request):
    return render(request,"shop/login.html")

def collections(request):
  catagery = Category.objects.filter(status=0)
  return render(request,"shop/collections.html",{"catagery":catagery})

def contact(request):
    return render(request,"shop/contact.html")

def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product=Products.objects.filter(category__name=name)
        return render(request,"shop/products/product.html",{"products":product,"category_name":name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            product=Products.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"product":product})
        else:
            messages.error(request,"No Such Produtct Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')
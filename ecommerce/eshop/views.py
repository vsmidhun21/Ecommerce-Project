from django.shortcuts import redirect, render
from .models import Category, Products
from django.contrib import messages
from eshop.form import CustomUserForm

def home(request):
  products=Products.objects.filter(trending=1)
  return render(request,"shop/index.html",{"products":products})

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
        return render(request,"shop/products/product.html",{"product":product,"category_name":name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            product=Products.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":product})
        else:
            messages.error(request,"No Such Produtct Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})
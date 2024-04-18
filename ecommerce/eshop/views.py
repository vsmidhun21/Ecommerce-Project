from django.shortcuts import redirect, render
from .models import Category, Products, Cart, Favorite
from django.contrib import messages
from eshop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.http import  JsonResponse

def home(request):
    products=Products.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

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
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registration Success You can Login Now..!")
                return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        return redirect("/")

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Products.objects.get(id=product_id)
        if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already in Cart'}, status=200)
            else:
                if product_status.quantity>=product_qty:
                    Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Added to Cart'}, status=200)
                else:
                    return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favorite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        return redirect("/")

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Products.objects.get(id=product_id)
        if product_status:
            if Favorite.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already in Favourite'}, status=200)
            else:
                Favorite.objects.create(user=request.user,product_id=product_id)
                return JsonResponse({'status':'Product Added to Favourite'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add Favourite'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def remove_fav(request,fid):
    item=Favorite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"shop/index.html")

def login(request):
    return render(request,"shop/login.html")

def collections(request):
    return render(request,"shop/collections.html")

def contact(request):
    return render(request,"shop/contact.html")
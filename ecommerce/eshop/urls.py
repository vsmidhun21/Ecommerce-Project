from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('contact',views.contact,name="contact"),
]
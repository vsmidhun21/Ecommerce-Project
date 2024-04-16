from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('collections',views.collections,name="collections"),
    path('contact',views.contact,name="contact"),
]
"""OE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    # path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('signin',views.register,name="register"),
    path('add/',views.add,name="add"),
    path('contact',views.contactus,name="contactus"),
    path('thank',views.thank,name="thank"),
    path('forgot',views.forgot,name="forgot"),
    path('login', views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('profile/<str:username>',views.profile, name="profile"),
    path('prodview/<str:ids>', views.productView , name="Productview"),
    path('checkout/<str:p_id>', views.checkout, name="checkout"),
    path('order', views.orders , name="orders")
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
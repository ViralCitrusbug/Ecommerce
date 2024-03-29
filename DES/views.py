from math import ceil, remainder
from operator import ipow
from unicodedata import category
from webbrowser import get
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse, request
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from DES.models import product,contact,profile
# Create your views here.


def Home(request):
    p = product.objects.all()
    n = len(p)
    nSlides = n//4 + ceil(n/4) - (n//4)
    c = {
        "product" : p,
        "len" : n,
        "no_of_slide" : nSlides,
        "range" : range(nSlides)
    }
    return render(request,'home.html',c)

def aboutus(r):
    return render(r,'aboutus.html')
def support(r):
    return render(r,'support.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # phone = request.POST.get('phone')
        email = request.POST.get('email')
        query = request.POST.get('Query')
        contacts = contact.objects.create(name = name, query = query , email =email)
        contacts.save()
        return redirect('thank')
    return render(request, 'contactus.html')
def add(request):
    if request.method == "POST":
        name = request.POST.get('pname')
        category = request.POST.get('cat')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        disc = request.POST.get('disc')
        image = request.FILES['img']
        prod = product.objects.create(product_name = name, product_category = category, product_desc = desc, product_price=price, product_disc = disc, product_image = image)
        prod.save()
        # print(image)
    return render(request,'add.html')
def thank(r):
    action = r.GET.get('action')
    print(action)
    c = {
        "action" : action
    }
    return render(r, 'thank.html', c)

def forgot(r):
    if r.method == "POST":
        email = r.POST.get('email')
        print(email)
    return render(r, 'forget.html')

def login(r):
    if r.method == "POST":
        name = r.POST.get('uname')
        passw = r.POST.get('pass')
        user = authenticate(username = name , password = passw)
        if user is None:
            messages.warning(r,"Incorrect Username or password !")
        auth.login(r, user)
        messages.success(r, "You are logged in")
        return redirect('home')
    return render(r, 'login.html')

def register(request):
    if request.method == "POST":
        first = request.POST.get('fname')
        last = request.POST.get('lname')
        uname = request.POST.get('uname')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        email = request.POST.get('email')
        # print(first,last,username,password1,password2,email)
        if password1 == password2 :
            user = User.objects.create(first_name = first , last_name = last , email = email , password = make_password(password1) , username = uname)
            user.save()
            return redirect('login')    
        else:
            messages.info(request,"Password Doesn't match")
            return redirect('register')
    return render(request, "register.html")

def logout(r):
    auth.logout(r)
    return redirect('login')

def profile(request,username):
    user = User.objects.filter(username = username).first()
    action = request.GET.get('action')
    print(action)
    c = {
        "user" : user,
        "action":action
    }
    return render(request, 'profile.html',c)

def productView(request, ids) :
    p = product.objects.filter(Product_id = ids).first()
    c = {
        "product" : p
    }
    return render(request , "productview.html",c)


def checkout(request, p_id):
    p =product.objects.filter(product_id = p_id).first()
    price = p.product_price
    discount = p.product_disc
    total = price - (price * (discount/100))
    c = {
        "product" : p,
        "amount" : total
    }
    return render(request, 'checkout.html',c)


def orders(request):
    return render(request , 'orders.html')
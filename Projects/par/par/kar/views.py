from django.shortcuts import render,redirect
from django.http import HttpResponse
from urllib import request
from django.views import View
from . models import Product,Customer,Cart
from . forms import RegistrationForm,CustomerProfileForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"kar/home.html")

def about(request):
    return render(request,"kar/about.html")

def contact(request):
    return render(request,"kar/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"kar/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"kar/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"kar/productdetail.html",locals())

class RegistrationView(View):
    def get(self,request):
        form= RegistrationForm()
        return render(request,'kar/registration.html',locals())
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulation! User registered")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"kar/registration.html",locals())


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"kar/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,city=city,locality=locality,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile saved Successfully")
        else:
            messages.warning(request,"Invalid Input Data")

        return render(request,"kar/profile.html",locals())
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,"kar/address.html",locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add= Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,"kar/Updateaddress.html",locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Update successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")
        # return render(request,"kar/Updateaddress.html",locals())

# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product=Product.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect("/cart")

# def show_cart(request):
#     user= request.user
#     cart=Cart.objects.filter(user=user)
#     return render(request,'kar/addtocart.html',locals())


def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("cart/")

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request,'kar/addtocart.html',locals())
# class MyPasswordResetView(View):
#     def get(self,request):
#         return render(request,"kar/reset.html",locals())

class Checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famout = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famout + 40
        return render(request,"kar/checkout.html",locals())
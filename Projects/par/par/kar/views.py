from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import RegistrationForm
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


class OrderView(View):
    def get(self, request):
        # orders = Order.objects.all()  # Retrieve all orders from the database
        return render(request, "kar/orders.html"
                    #   , {'orders': orders}
                    )

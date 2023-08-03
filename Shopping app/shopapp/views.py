from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from shopapp.form import CustomUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    products=product.objects.filter(trending=1)
    return render(request,'shopapp/index.html',{"products":products})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            name=request.POST.get("username")
            pwd=request.POST.get("Password")
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in succesfully")
                return redirect("/")

            else:
                messages.error(request,"Invalid User Name or Password")
        return render(request,'shopapp/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Succesfully")
    return redirect("/")


def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success You can login now")
            return redirect("/login")
    return render(request,'shopapp/register.html',{"form":form})

def collection(request):
    Catagory=catagory.objects.filter(status=0)
    return render(request,'shopapp/collection.html',{"catagory":Catagory})

def collectionview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(catagory__name=name)
        return render(request,"shopapp/product/index.html",{"products":products,"catagory_name":name})
    else:
        messages.warning(request,"no such category")
        return redirect('collection')

def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
       
       if(product.objects.filter(product_name=pname,status=0)):
            products=product.objects.filter(product_name=pname).first()
            return render(request,"shopapp/product/product_details.html",{"products":products})
       else:
            messages.error(request,"no such products found")
            return redirect('collection')
    else:
        messages.error("no such catagory")
        return redirect('collection')



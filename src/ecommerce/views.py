from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def home_page(request):
    context={
        "title":"We're working on it!!",
        "content":"welcome to home page",
        
       
    }
    if request.user.is_authenticated:
        context["Premium"]="Yaaah"
    return render(request, "home_page.html", context)

def About(request):
    context={
        "title":"We're working on it!!",
        "content":"welcome to about page"
        
    }
    return render(request, "home_page.html", context)

def Contact(request):
    contactForm = ContactForm(request.POST or None)
    context={
        "title":"We're working on it!!",
        "content":"welcome to contact page",
        "form" : contactForm
    }
    if contactForm.is_valid():
        print(contactForm.cleaned_data)
    # if request.method == "POST":
    #      print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))


    return render(request, "contact.html", context)


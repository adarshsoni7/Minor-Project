from django.shortcuts import render
from .models import Destination
from .models import Blogs
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

def index(request):

    dests = Destination.objects.all()

    return render(request, "./index.html", {'dests': dests})


def blog(request):
    blogs = Blogs.objects.all()
    return render(request, "./blog.html", {'blogs': blogs})


def blogindex(request):
    blogs = Blogs.objects.all()
    return render(request, "./index1.html", {'blogs': blogs})


def contact(request):
    return render(request, "./contact.html")


def about(request):
    return render(request, "./about.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
            "message" : "Invalid Credentials"
            })
    return render(request, "login.html")
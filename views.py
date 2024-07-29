from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def lib(request):
    return render(request, "lib.html", context={})


def user(request):
    return render(request, "user.html", context={})
def ad(request):
    return render(request,"ad.html",context={})

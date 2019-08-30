from django.shortcuts import render
from .models import Item


def item_list(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "home.html", context)


def checkout(request):
    context = {}
    return render(request, "checkout.html", context)


def product(request):
    context = {}
    return render(request, "product.html", context)

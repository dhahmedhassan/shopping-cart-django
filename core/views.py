from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


def checkout(request):
    context = {}
    return render(request, "checkout.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


# def product(request):
#     context = {}
#     return render(request, "product.html", context)

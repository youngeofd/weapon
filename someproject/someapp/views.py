from django.http import Http404
from django.shortcuts import render

from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "someapp/catalog.html", {"products": products})


def product_detail(request, slug: str):
    product = Product.objects.filter(slug=slug).first()
    if not product:
        raise Http404("Товар не найден")
    return render(request, "someapp/product_detail.html", {"product": product})

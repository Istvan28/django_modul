from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        "title": "Home - Fő oldal",
        "content": "Магазин мебели HOME",
        # "list": ["first", "second"],
        # "dict": {"first": 1},
        # "is_authenticated": True,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - Amit tudnod kell",
        "content": "Магазин мебели HOME",
        "text_on_page": "Amit tudnod kell",
        # "list": ["first", "second"],
        # "dict": {"first": 1},
        # "is_authenticated": True,
    }
    return render(request, "main/about.html", context)

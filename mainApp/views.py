from django.shortcuts import render
from .models import *
from urllib.parse import unquote


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    maqolalar = Maqola.objects.all()
    content = {
        "maqolalar": maqolalar
    }
    return render(request, "blog.html", content)


def maqola(request, link):
    segments = link.rsplit('/', 2)
    slug = segments[-1].rstrip('/')
    decoded_slug = unquote(slug).replace("-", " ").title()
    data = Maqola.objects.filter(title=decoded_slug).first()
    content = {
        "data": data
    }
    return render(request, 'maqola.html', content)

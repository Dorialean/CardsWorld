from django.shortcuts import render


def index(request):
    return render(request, 'face/index.html', None)


def register(request):
    return render(request, "face/register.html")

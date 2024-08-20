from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "msg": "Welcome to Django"
    }
    return render(request, "webcms/index.html", context)


def menu(request):
    context = {
        "msg": "Menu Page"
    }
    return render(request, "webcms/menu.html", context)

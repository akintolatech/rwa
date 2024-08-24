from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "msg": "Welcome to Django"
    }
    return render(request, "webcms/pages/index.html", context)


def menu(request):
    context = {
        "msg": "Menu Page"
    }
    return render(request, "webcms/pages/menu.html", context)

def about(request):
    context = {
        "msg": "About Page"
    }
    return render(request, "webcms/pages/about.html", context)

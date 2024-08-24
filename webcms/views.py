from django.shortcuts import render
from .models import WebDetails


# Create your views here.
def index(request):

    business = WebDetails.objects.get(id=1)
    context = {
        "business": business
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

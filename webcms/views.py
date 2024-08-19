from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "msg": "Welcome to Django"
    }
    return render (request, "webcms/index.html", context)

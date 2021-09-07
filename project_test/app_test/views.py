from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def greet(request, user="User"):
    return render(request, "app_test\\index.html", context={
        "username" : user.capitalize()
    })

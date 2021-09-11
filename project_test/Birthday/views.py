from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    print("Request -", request)
    now = datetime.datetime.now()
    return render(request, "Birthday\\index.html", context = {
        "value": now.month == 1 and now.day == 10
    })

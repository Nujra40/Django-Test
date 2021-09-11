from django.forms.fields import CharField
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks\\index.html")

def view(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks\\view.html", context={
        "tasks": request.session["tasks"]
    })

def add(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            print(form.cleaned_data)
            request.session["tasks"] += [task]
            
            return HttpResponseRedirect(reverse('tasks:view'))

    return render(request, "tasks\\add.html", context= {
        "form": NewTaskForm()
    })
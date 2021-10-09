from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
class NewForm(forms.Form):
    new_task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [] 

    return render(request , "tasks/index.html" , {"tasks" : request.session["tasks"] })

def add(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            task  = form.cleaned_data["new_task"]
            if task in request.session["tasks"]:
                return render(request ,"tasks/add.html" , {"form": form , "message":"*This task already exists"})
            else:
                request.session["tasks"] += [task] 
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request ,"tasks/add.html" , {"form": form})
    
    return render(request , "tasks/add.html",{"form": NewForm()}    ) 

def delete(request , name):
    request.session["tasks"].remove(name)
    request.session.modified = True
    return  HttpResponseRedirect(reverse("tasks:index"))
def clear(request):
    try:
        del request.session["tasks"]
    except :
        pass 
    return HttpResponseRedirect(reverse("tasks:index"))


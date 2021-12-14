from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.settings import MEDIA_ROOT
from .models import ToDoList, Item
from .forms import CreateNewList, UploadFileForm
import pandas as pd
from .ml import getResult

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    #item = ls.item_set.get(id=1)
    return render(response, "main/list.html", {"ls":ls})
    #return HttpResponse("<h1> the id is %s</h1>" %name)
    #return HttpResponse("<h1>the id is %s</h1><br></br><p>%s</p>"  %(ls.name,str(item.text)))
    #now it will get the list with id = the number after url. eg /1 would get the ToDoList with id 1
    #can also use strings instead of int for id, etc.
def intTest(response, id):
    return HttpResponse("<h1>%s</h1>" % id)

def predict(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print("massive success")
        if form.is_valid():
            print("valid")
            file = request.FILES['file']   
            data = pd.read_csv(file)
            result = getResult(data)
            return render(request,'main/result.html',{"score": result})
            #print(data.head())
            #print(MEDIA_ROOT)
            #file_name = MEDIA_ROOT.save(file.name, file)
        else:
            print(form._errors)
    else:
        print("failed")
        form = UploadFileForm() 
    return render(request, "main/predict.html", {"form":form})
def test(response):
    return HttpResponse("<h1> testing screen </h1>")
def home(response):
    return render(response, "main/home.html", {})
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList() 
    return render(response, "main/create.html", {"form":form})
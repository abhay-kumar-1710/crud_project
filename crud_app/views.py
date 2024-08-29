from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from crud_app.forms import PersonDataForm
from crud_app.models import PersonData


# Create your views here.

def home(request):
    data = PersonData.objects.all()
    if request.method == "POST":
        form = PersonDataForm(request.POST)
        form.save()
        form = PersonDataForm()
    else:
        form = PersonDataForm()
    return render(request, 'crud_app/home.html', {"form" : form, "data" : data})

def update(request, id):
    
    if request.method == "POST":
        data = PersonData.objects.get(pk=id)
        form = PersonDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        data = PersonData.objects.get(pk=id)
        form = PersonDataForm(instance=data)
    return render(request, 'crud_app/update.html', {"form" : form})

def delete(request,id):
    data = PersonData.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/')
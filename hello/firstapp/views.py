from django.http import *
from .forms import UserForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


# получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в БД
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


# изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


# удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")





def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def products(request):
    productid = request.GET.get('id', 2)
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0}</h2> <h3> Категория: {1}</h3>" .format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0}  Имя: {1}</h3 >" .format(id, name)
    return HttpResponse(output)



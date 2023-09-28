from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.response import TemplateResponse
from .models import Person


def index(request):
    return TemplateResponse(request, "index.html", context={'header' : 'Testing django', 'message' : 'hello user!'})

def user(request):
    age = request.GET.get('age')
    name = request.GET.get('name')
    return HttpResponseBadRequest("Доступ заблокирован: недостаточно лет")

def postuser(request):
    name = request.POST.get('name', 'Underfined')
    age = request.POST.get('age', 1)
    Person(name = name, age = age).save()
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")

def persons(request):
    persons_count = Person.objects.count()
    persons = []
    for person in Person.objects.all():
        persons.append(person.name)
    return HttpResponse(f"<h2>Persons count {persons} </h2>")
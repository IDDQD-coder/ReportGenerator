from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import Person



def start_page(request):
    return HttpResponse(f"""<a href = "/accounts/login">ENTER</a>""")


@login_required
def home(request):
    user = str(request.user)
    print(user)
    return TemplateResponse(request, "home.html",context={'name':user})
    
@login_required
def user(request):
    age = request.GET.get('age')
    name = request.GET.get('name')
    return HttpResponseBadRequest("Доступ заблокирован: недостаточно лет")

@login_required
def newperson(request):
    return TemplateResponse(request, "newperson.html")

@login_required
def postuser(request):
    name = request.POST.get('name', 'Underfined')
    age = request.POST.get('age', 1)
    Person(name = name, age = age).save()
    return HttpResponse(f"<h2> Person created! Name: {name}  Age: {age}</h2>")

@login_required
def persons(request):
    persons_count = Person.objects.count()
    persons = []
    for person in Person.objects.all():
        persons.append(person.name)
    return HttpResponse(f"<h2>Persons count {persons} </h2>")
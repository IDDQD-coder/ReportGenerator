from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.response import TemplateResponse

def index(request):

    return TemplateResponse(request, "index.html", context={'header' : 'Testing django', 'message' : 'hello user!'})

def user(request):
    age = request.GET.get('age')
    name = request.GET.get('name')
    return HttpResponseBadRequest("Доступ заблокирован: недостаточно лет")

from django.urls import path

from . import views

urlpatterns = [
    path("", views.start_page, name="index"),
    path("newperson/", views.newperson, name='newperson'),
    path("user/", views.user, name='user'),
    path("newperson/postuser/", views.postuser, name = 'postuser'),
    path("persons/",views.persons, name='persons'),
    path("home/",views.home, name='home')
]
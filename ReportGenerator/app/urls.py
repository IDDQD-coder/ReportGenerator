from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name='user'),
    path("postuser/", views.postuser, name = 'postuser'),
    path("persons/",views.persons, name='persons')
]
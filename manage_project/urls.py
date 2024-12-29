from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("list/", views.list, name="list"),
    path("Add_Donner/", views.Add_Donner, name="Add_Donner"),
    path("A_pos/", views.A_pos, name="A_pos"),
    path("A_neg/", views.A_neg, name="A_neg"),
    path("AB_pos/", views.AB_pos, name="AB_pos"),
    path("AB_neg/", views.AB_neg, name="AB_neg"),
    path("B_pos/", views.B_pos, name="B_pos"),
    path("B_neg/", views.B_neg, name="B_neg"),
    path("O_pos/", views.O_pos, name="O_pos"),
    path("O_neg/", views.O_pos, name="O_neg"),
    path('search/', views.search, name='search'),
]

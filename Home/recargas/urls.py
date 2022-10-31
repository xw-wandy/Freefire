from django.urls import path
from . import views


app_name = "recargas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:numero>/", views.registro, name="registro"),
    path("verificar/", views.verificar, name="verificar"),
    path("esperar/", views.esperar, name="esperar"),
    path("info/", views.info, name="info")
]



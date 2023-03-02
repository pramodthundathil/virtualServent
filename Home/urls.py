from django.urls import path
from .import views

urlpatterns = [
    path("AddMenu",views.AddMenu,name="AddMenu"),
    path("ViewMenu",views.ViewMenu,name="ViewMenu"),
]

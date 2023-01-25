from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<idx>", views.detail, name="detail"),
    path("delete/<idx>", views.delete, name="delete"),
]

from django.urls import path
from testdb import views

urlpatterns = [
    path("", views.index)
]

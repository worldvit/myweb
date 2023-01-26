from django.urls import path,include
from . import views

urlpatterns = [
    path ('index/', views.index, name='index'),
    path ('create/', views.create, name='create'),
    path ('delete/<idx>', views.delete, name='delete'),
]
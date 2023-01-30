from django.urls import path,include
from phonebook import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('detail/<idx>', views.detail, name='detail'),
    path('update/', views.update, name='update'),
]
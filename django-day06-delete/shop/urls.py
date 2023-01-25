from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<idx>', views.delete, name='delete'),
    path('detail/<idx>',views.detail, name='detail'),
    path('create/',views.create, name='create'),
    path('update/<idx>',views.update, name='update'),
]

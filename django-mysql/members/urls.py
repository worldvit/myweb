from django.urls import path
from members import views

urlpatterns = [
    path('index/', views.members),
]

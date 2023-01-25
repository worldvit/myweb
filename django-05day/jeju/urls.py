from django.urls import path,include
from jeju import views

urlpatterns = [
    path('', views.jeju)
]

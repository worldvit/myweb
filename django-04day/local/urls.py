from django.urls import path,include
from local import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jeju/', views.jeju, name='jeju'),
    path('seoul/', views.seoul,name='seoul'),
]
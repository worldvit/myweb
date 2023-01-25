from django.urls import path,include
from local import views


urlpatterns = [
    path('jeju/', views.jeju),
    path('seoul/', views.seoul),
]
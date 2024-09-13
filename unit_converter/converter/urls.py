from django.urls import path
from . import views

app_name = 'converter'
urlpatterns = [
    path('', views.temperature, name='temperature'),
    path('lenght/', views.lenght, name='lenght'),
    path('weight/', views.weight, name='weight'),
]
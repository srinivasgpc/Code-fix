from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name='home'), 
    path('operator', views.operator, name='operator')
]
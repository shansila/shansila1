from django.urls import path
from . import views

urlpatterns =[
    path('', views.fun),
    path('type',views.fun1),
    path('type1',views. fun2)
]
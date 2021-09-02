from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<str:room>', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
]

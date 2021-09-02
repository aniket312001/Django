from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.apprun, name="run"),
    path('user/', views.display_user, name='user'),
    path('form/', views.app_form, name='form'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    
]
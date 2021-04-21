from django.urls import path

from . import views

urlpatterns = [
    #('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
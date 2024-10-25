from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', show_departments, name='show_departments'),
    path('<int:pk>/employees/', employees_lst, name='employees_lst'),
    path('<int:pk>/employees/<int:employee_pk>/',
         employee_retrieve,
         name='employee_retrieve'),
]
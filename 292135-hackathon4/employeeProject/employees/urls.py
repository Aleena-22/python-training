from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'), 
    path('form/', views.employee_form, name='employee_form'),
    path('calculate/', views.calculate_net_salary, name='calculate'),
    path('jumble/', views.jumble_word, name='jumble'),
]




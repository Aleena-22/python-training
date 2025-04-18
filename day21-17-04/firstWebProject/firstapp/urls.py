from django.urls import path
from . import views

urlpatterns = [
    path('converter/', views.converter_view, name='converter'),
    path('timer/', views.timer_view, name='timer')
]

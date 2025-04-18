from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home') # 127.0.0.1:8000/ -> run a function called home in views
# ]

urlpatterns = [
    path('', views.index_view, name='index'),
]
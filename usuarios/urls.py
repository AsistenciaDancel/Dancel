from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.dashboard, name='usuarios_dashboard'), 
]

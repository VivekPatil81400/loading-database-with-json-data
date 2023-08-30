from django.urls import path
from . import views

urlpatterns = [
    path('create-instance/', views.create_instance_view, name='create-instance'),
]
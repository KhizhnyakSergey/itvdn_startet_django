from django.urls import path
from lesson_5 import views

urlpatterns = [
    path('create-flower/', views.create_flower, name='create-flower'),
    path('create-client/', views.create_client, name='create-client'),
    path('get-flower/', views.get_flower, name='get-flower'),
]

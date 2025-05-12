from django.urls import path
from workers import views

urlpatterns = [
    path('create/', views.create_worker, name='create_worker'),
    path('', views.worker_list, name='worker_list'),
]
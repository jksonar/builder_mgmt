from django.urls import path
from tasks import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('', views.task_list, name='task_list'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
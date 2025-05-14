from django.urls import path
from projects import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('', views.project_list, name='project_list'),
    path('edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),
]
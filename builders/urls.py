from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_builder_company, name='create_builder_company'),
    path('', views.builder_company_list, name='builder_company_list'),
    path('edit/<int:pk>/', views.edit_builder_company, name='edit_builder_company'),
    # path('', views.builder_list, name='builder_list'),
    path('create/', views.create_builder, name='create_builder'),
]
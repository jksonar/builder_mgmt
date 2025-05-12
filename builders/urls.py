from django.urls import path
from builders import views

urlpatterns = [
    path('create/', views.create_builder, name='create_builder'),
    path('', views.builder_list, name='builder_list'),
]
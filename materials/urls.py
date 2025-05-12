from django.urls import path
from materials import views

urlpatterns = [
    path('create/', views.create_material, name='create_material'),
    path('', views.material_list, name='material_list'),
]
from django.urls import path
from payments import views

urlpatterns = [
    path('create/', views.create_payment, name='create_payment'),
    path('', views.payment_list, name='payment_list'),
]
from django.urls import path
from attendance import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('', views.attendance_list, name='attendance_list'),
]
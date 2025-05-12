from django.urls import path
from issues import views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('', views.issue_list, name='issue_list'),
]
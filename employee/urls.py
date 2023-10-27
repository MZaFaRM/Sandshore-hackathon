from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeAPI.as_view(), name='employee-list-create'),
    path('employees/<str:pk>/', views.EmployeeAPI.as_view(), name='employee-detail'),
    path('eligible-employees/', views.EligibleEmployees.as_view(), name='eligible-employee'),
    path('departments/', views.DepartmentAPI.as_view(), name='department-list-create'),
    path('departments/<str:pk>/', views.DepartmentAPI.as_view(), name='department-detail'),
]

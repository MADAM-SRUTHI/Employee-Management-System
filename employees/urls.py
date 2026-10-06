from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('search/', views.search_employee, name='search_employee'),
    path('employee/<int:id>/', views.employee_profile, name='employee_profile'),
]
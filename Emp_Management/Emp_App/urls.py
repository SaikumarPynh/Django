from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Add Employee Page
    path('Add_Emp', views.add_emp, name="Add_Emp"),

    # All Employees Page
    path('All_Emp', views.all_emp, name="All_Emp"),

    # Remove Employee Page (with optional employee ID parameter)
    path('Remove_Emp', views.remove_emp, name="Remove_Emp"),
    path('remove_emp/<int:emp_id>', views.remove_emp, name="Remove_Emp"),

    # Filter Employees Page
    path('filter_emp', views.filter_emp, name='Filter_Emp'),
]

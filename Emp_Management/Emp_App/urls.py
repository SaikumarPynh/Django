from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('Add_Emp' , views.add_emp, name = "Add_Emp"),
    path('All_Emp' , views.all_emp, name = "All_Emp"),
    path('Remove_Emp' , views.remove_emp, name = "Remove_Emp"),
    path('filter_emp', views.filter_emp, name='Filter_Emp'),

    path('remove_emp/<int:emp_id>' , views.remove_emp, name = "Remove_Emp"),

]

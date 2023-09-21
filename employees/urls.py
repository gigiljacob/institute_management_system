from django.urls import path

from employees.views import EmployeeList, EmployeeCreate

app_name = 'employees'
api_version = 'v1'

urlpatterns = [
    path('list/institute/<ins_identifier>/', EmployeeList.as_view(), name='list'),
    path('create/institute/<ins_identifier>/', EmployeeCreate.as_view(), name='create'),
]

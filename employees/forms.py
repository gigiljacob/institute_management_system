from django import forms
from django.forms import ModelForm

from accounts.forms import ImsUserCreationForm
from employees.models import Employee

#
# class EmployeeForm(ModelForm):
#
#     class Meta:
#         model = Employee
#         fields = '__all__'

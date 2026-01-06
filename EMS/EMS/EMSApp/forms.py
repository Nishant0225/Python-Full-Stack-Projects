from django.forms import *
from . import models

class EmployeeModelForm(ModelForm):
    class Meta:
        model=models.EmployeeModel
        fields='__all__'

        widgets={
            'dept':Select(choices=[('Accounts','Accounts'),('HR','HR'),('IT','IT'),('Sales','Sales')]),
            'job':Select(choices=[('Clerk','Clerk'),('Developer','Developer'),('Manager','Manager'),('Accountant','Accountant')]),
            'gender':RadioSelect(choices=[('Male','Male'),('Female','Female')])

        }
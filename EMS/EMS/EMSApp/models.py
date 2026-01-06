from django.db.models import *

# Create your models here.

class EmployeeModel(Model):
    empid=IntegerField(primary_key=True)
    name=CharField(max_length=100)
    email=EmailField(max_length=100)
    contact=IntegerField(max_length=100)
    dept=CharField()
    job=CharField()
    salary=IntegerField()
    gender=CharField()
    city=CharField(max_length=100)

    
from django.shortcuts import render , HttpResponse,redirect
from . import forms
from .import models
from django.contrib import messages
from django.core.paginator import *

# Create your views here.

def index(request):
   
    return render(request,"index.html")

def dashboard(request):
    totalemp=models.EmployeeModel.objects.count()
    employees=models.EmployeeModel.objects.all()
    s=0
    for emp in employees:
      s=s+emp.salary 
    avgsalary=round(s/totalemp)  
    totaldept=4   
    return render(request,"dashboard.html",{'totalemp':totalemp,'avgsalary':avgsalary,'totaldept':totaldept })
    
def addemp(request):
    if request.method=="POST":
        form=forms.EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee Saved...")
        else:
            return render(request,"addemp.html",{'form':form})    
    form=forms.EmployeeModelForm()
    return render(request,"addemp.html",{'form':form})

def listemp(request):
    employees=models.EmployeeModel.objects.all()
    paginator=Paginator(employees,2)
    page_num=request.GET.get('page',1)
    pageEmps=paginator.get_page(page_num)
    page_obj=paginator.page(page_num)
    return render(request,"listemp.html",{'employees':pageEmps,'page_obj':page_obj})

def searchemp(request):
    if request.method=="POST":
        empname=request.POST.get('empname')
        employees=models.EmployeeModel.objects.filter(name__icontains=empname)
        return render(request,"searchemp.html",{'employees':employees})
    return render(request,"searchemp.html")

def deleteemp(request,id):
    models.EmployeeModel.objects.get(empid=id).delete()
    messages.success(request,"Employee Deleted..")
    return redirect("listemp")
    

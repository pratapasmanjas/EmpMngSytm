from django.shortcuts import render, HttpResponse
from django.template.defaulttags import csrf_token

from .models import employee, Role, Dept
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        new_emp = employee(first_name=first_name, last_name=last_name, department_id=department,
                           salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('NEW EMPLOYEE ADDED SUCCESSFULLY')
        return render(request,'add_emp.html')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('an exception Occur !! employee not added')


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee removed successfully")
        except:
            return HttpResponse("pleas enter a valid employee ID")
    emps = employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request,):
    # name = request.POST.get('name',False)
    # {%csrf_token%}
    if request.method =='POST':

        name = request.POST.get['name'],
        dept = request.POST.get['department'],
        role = request.POST.get['role'],
        emps = employee.objects.all()

        if name:

            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name=role)
        context = {
           ' emps': emps
        }
        return render(request,'all_emp.html',context)
    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        HttpResponse('Invalid credential are used!!')


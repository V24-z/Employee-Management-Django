from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from .models import Employee,Department,Role
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.db.models import Q
from .forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator
def index(request):
    
    return render(request,'index.html')

def view_emp(request):
    emps = Employee.objects.all().order_by('id')

    if request.method == 'POST':
        return redirect('index')

    name = request.GET.get('name')
    dept = request.GET.get('dept')
    role = request.GET.get('role')

    if name:
        emps = emps.filter(
            Q(first_name__icontains=name) |
            Q(last_name__icontains=name)
        )

    if dept:
        emps = emps.filter(dept__name__icontains=dept)

    if role:
        emps = emps.filter(role__name__icontains=role)

    #  Pagination (10 records per page)
    paginator = Paginator(emps, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'emps':emps,
        'name': name,
        'dept': dept,
        'role': role,
    }

    return render(request, 'view_emp.html', context)


@csrf_exempt
def add_emp(request):
    if request.method == 'POST':
        emps = EmployeeForm(request.POST, request.FILES)
        if emps.is_valid():
            emps.save()
        messages.success(request, "Data inserted successfully")   
        return redirect( 'view_emp') # optional
    else:
        emps = EmployeeForm()   # ✅ create empty form

    context = {'emps': emps}
    return render(request, 'add_emp.html', context)
    




"""   if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
      
        new_emp=Employee(first_name=first_name,last_name=last_name,
                         dept_id=dept,salary=salary,bonus=bonus,phone=phone,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return  HttpResponse("record successfully added!!")
    elif request.method=='GET':
         return render(request,'add_emp.html')
    else:   
        return  HttpResponse("Exception occured!!employee has not added!!") """

def remove_emp(request ,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            messages.success(request, f"remove successfuly!!{emp_id}")   
            return redirect('view_emp')
        except:
            return HttpResponse("please enter valid emp name") 
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html', context)
   
def update_emp(request, id):
    emps = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=emps)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully")
            return redirect('view_emp')
    else:
        emps = EmployeeForm(instance=emps)

    return render(request, 'update_emp.html', {'emps': emps})

def filter_emp(request):
     if request.method =='GET':
         name = request.GET.get('name')          # ✅ safe
         dept = request.GET.get('dept')
         role = request.GET.get('role')

         emps=Employee.objects.all()
         if name:
             emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
         if dept:
             emps=emps.filter(dept__name__icontains=dept)
         if role:
              emps=emps.filter(role__name__icontains=role)
         context={
            'emps':emps
              }
         return render(request,'view_emp.html',context)
     elif request.method=='GET':
                return render(request,'filter_emp.html')
     else:
          return HttpResponse("ERROR OCCURE!!!")


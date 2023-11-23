from django.shortcuts import render,HttpResponse
from .models import Role,Employee,Department
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all
    context = {
        'emps' : emps
        }
    
    print(context)
    return render(request, "All_Emp.html", context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        salary = int(request.POST["salary"])
        phone = int(request.POST["phone"])
        bonus = int(request.POST["bonus"])
        hire_date = request.POST["hire_date"]
        dept_name = request.POST["dept"]
        role_name = request.POST["role"]

        dept, created = Department.objects.get_or_create(name=dept_name)

        # Get or create Role
        role, created = Role.objects.get_or_create(name=role_name)

        new_emp = Employee(first_name = first_name,last_name = last_name,salary = salary,phone = phone,bonus = bonus,hire_date = hire_date,dept = dept, role = role)
        new_emp.save()
        return HttpResponse("successfull")
    elif request.method == "GET":

        return render(request, "Add_Emp.html")
    else:
        return HttpResponse("An Exception Occured")
    
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:

            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee deleted from database")
        except:
            return HttpResponse("please enter a valid response")
    emps = Employee.objects.all
    context = {
        'emps' : emps
        }
    return render(request, "Remove_Emp.html", context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name)) 
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
        context = {'emps' : emps}
        return render(request, 'All_Emp.html',context)
    return render(request, "Filter_Emp.html")
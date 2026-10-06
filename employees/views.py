from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Employee


@login_required
def dashboard(request):
    employees = Employee.objects.all().order_by('-id')

    total_employees = employees.count()
    departments = employees.values('department').distinct().count()

    context = {
        'employees': employees,
        'total_employees': total_employees,
        'departments': departments,
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_employee(request):

    if request.method == 'POST':

        Employee.objects.create(
            employee_id=request.POST['employee_id'],
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            position=request.POST['position'],
            salary=request.POST['salary'],
            joining_date=request.POST['joining_date']
        )

        return redirect('dashboard')

    return render(request, 'add_employee.html')


@login_required
def update_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':

        employee.employee_id = request.POST['employee_id']
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.position = request.POST['position']
        employee.salary = request.POST['salary']
        employee.joining_date = request.POST['joining_date']

        employee.save()

        return redirect('dashboard')

    return render(
        request,
        'update_employee.html',
        {'employee': employee}
    )


@login_required
def delete_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':

        employee.delete()

        return redirect('dashboard')

    return render(
        request,
        'delete_employee.html',
        {'employee': employee}
    )


@login_required
def search_employee(request):

    query = request.GET.get('q', '').strip()

    employees = Employee.objects.filter(
        Q(name__icontains=query) |
        Q(employee_id__icontains=query) |
        Q(email__icontains=query) |
        Q(department__icontains=query)
    )

    context = {
        'employees': employees,
        'query': query,
    }

    return render(
        request,
        'search_results.html',
        context
    )


@login_required
def employee_profile(request, id):

    employee = get_object_or_404(Employee, id=id)

    return render(
        request,
        'employee_profile.html',
        {'employee': employee}
    )
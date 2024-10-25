from django.shortcuts import render

from tree_employees.models import Department, Employee

def index(request):
    """Эндпоинт начальной страницы"""
    root_departments = Department.objects.filter(parent=None)
    return render(request, 'tree_employees/index.html', {'root_departments': root_departments})

def show_departments(request, pk):
    """Эндпоинт для отрисовки дерева отделов"""
    return render(request, 'tree_employees/index.html', {'department_pk': pk})

def employees_lst(request, pk):
    """Эндпоинт отображения списка персонала конкретного отдела"""
    department = Department.objects.get(pk=pk)
    employees = Employee.objects.filter(department=department)
    return render(request, 'tree_employees/employees.html', {'employees': employees, 'department': department})

def employee_retrieve(request, pk, employee_pk):
    """Эндпоинт отображения информации о конкретном сотруднике"""
    employee = Employee.objects.get(pk=employee_pk)
    return render(request, 'tree_employees/employee.html', {'employee': employee, 'pk': pk})
from django.contrib import admin

from tree_employees.models import Employee, Department

admin.site.register(Employee)
admin.site.register(Department)

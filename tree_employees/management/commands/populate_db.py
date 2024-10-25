from random import choice, randint
from datetime import date, timedelta

from django.core.management.base import BaseCommand

from tree_employees.models import Department, Employee


class Command(BaseCommand):
    help = 'Populate the database with test employees and departments'

    def handle(self, *args, **kwargs):
        d1 = Department.objects.create(name='D1')

        d2 = Department.objects.create(name='D2', parent=d1)
        d3 = Department.objects.create(name='D3', parent=d1)

        d4 = Department.objects.create(name='D4', parent=d2)
        d5 = Department.objects.create(name='D5', parent=d2)
        d6 = Department.objects.create(name='D6', parent=d3)
        d7 = Department.objects.create(name='D7', parent=d3)

        d8 = Department.objects.create(name='D8', parent=d4)
        d9 = Department.objects.create(name='D9', parent=d4)
        d10 = Department.objects.create(name='D10', parent=d5)
        d11 = Department.objects.create(name='D11', parent=d5)
        d12 = Department.objects.create(name='D12', parent=d6)
        d13 = Department.objects.create(name='D13', parent=d6)
        d14 = Department.objects.create(name='D14', parent=d7)
        d15 = Department.objects.create(name='D15', parent=d7)

        d16 = Department.objects.create(name='D16', parent=d8)
        d17 = Department.objects.create(name='D17', parent=d8)
        d18 = Department.objects.create(name='D18', parent=d9)
        d19 = Department.objects.create(name='D19', parent=d9)
        d20 = Department.objects.create(name='D20', parent=d10)
        d21 = Department.objects.create(name='D21', parent=d10)
        d22 = Department.objects.create(name='D22', parent=d11)
        d23 = Department.objects.create(name='D23', parent=d11)
        d24 = Department.objects.create(name='D24', parent=d12)
        d25 = Department.objects.create(name='D25', parent=d12)
        departments = [
            d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15,
            d16, d17, d18, d19, d20, d21, d22, d23, d24, d25
        ]

        employee_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
        positions = ['Manager', 'Developer', 'Analyst', 'Designer',
                     'Salesperson']
        # Создание сотрудников
        for _ in range(50000):  # создадим 10 сотрудников
            name = choice(employee_names) + " " + str(
                randint(1, 100))
            position = choice(positions)
            date_of_employment = date.today() - timedelta(
                days=randint(1, 365 * 5))  # случайная дата трудоустройства
            salary = randint(30000, 100000)  # случайная зарплата
            department = choice(departments)

            Employee.objects.create(
                name=name,
                position=position,
                date_of_employment=date_of_employment,
                salary=salary,
                department=department
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with test data.'))

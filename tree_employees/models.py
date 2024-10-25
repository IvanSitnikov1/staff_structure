from django.db import models


class Employee(models.Model):
    """Модель сотрудника"""
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    date_of_employment = models.DateField()
    salary = models.FloatField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    """Модель отдела"""
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    def __str__(self):
        return self.name

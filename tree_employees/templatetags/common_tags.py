from django import template
from django.core.exceptions import ObjectDoesNotExist

from tree_employees.models import Department


register = template.Library()


# Пользовательский тег для отрисовки дерева отделов
@register.inclusion_tag('tree_employees/tree_departments.html')
def show_departments(department_pk=None):
    items = Department.objects.all()

    def build_departments_tree(department_pk=None, lst_sub_departments=None):
        """Функция собирает дерево отделов в список"""
        if department_pk:
            departments = list(items.filter(parent__pk=department_pk))
        else:
            departments = list(items.filter(parent=None))
        try:
            departments.insert(
                departments.index(lst_sub_departments[0].parent) + 1,
                lst_sub_departments)
        except (IndexError, TypeError):
            pass
        try:
            return build_departments_tree(
                items.get(pk=department_pk).parent.pk, departments)
        except AttributeError:
            return build_departments_tree(lst_sub_departments=departments)
        except ObjectDoesNotExist:
            return departments

    return {'departments': build_departments_tree(department_pk)}

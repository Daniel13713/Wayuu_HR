#!/usr/bin/python3

"""
--------------------------
Role Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from apps.management.models.department import Department
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee
from django.utils.translation import gettext_lazy as _


class Role(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)
    job_description = models.TextField()
    default_contract = models.CharField(max_length=100, default="Pdf option")
    default_salary = models.FloatField()

    employee = models.ManyToManyField(Employee, related_name="roles", through='Employee_Role')
    department = models.ManyToManyField(Department, related_name="roles_by_deparment", through='Department_Role')

    def __str__(self) -> str:
        return self.name

class Employee_Role(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Role tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        help_text="Date when employee start in role",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in role",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.role.__str__())

class Department_Role(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Role tables
    ----------------------------------
    """

    deparment = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        help_text="Date when the role was created",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "Role {} in department {}".format(self.role.__str__(), self.deparment.__str__())
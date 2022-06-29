#!/usr/bin/python3

"""
--------------------------
Salary Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee
from django.utils.translation import gettext_lazy as _

class Salary(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    amount = models.FloatField()
    contract = models.CharField(max_length=100, default="pdf option or collila de pago?")

    employee = models.ManyToManyField(Employee, through='Employee_Salary', related_name="salary")

    def __str__(self) -> str:
        return "There are {} employees with this salary".format(self.employee.count())


class Employee_Salary(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Salary tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        help_text=_("Date when you the company pays"),
        default=timezone.now
    )

    bonuses = models.FloatField(blank=True)
    paper_pay = models.CharField(max_length=100, default="pdf option", help_text="Colilla de pago")

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.salary.__str__())
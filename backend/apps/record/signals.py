"""
---------------------------------------
Signal to Record tables
---------------------------------------
"""
import logging

from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from apps.record.models import Resume
from admin_project.settings.base import AUTH_USER_MODEL
from apps.sys_admin.models.employee import Employee
from apps.management.models import *

logger = logging.getLogger(__name__)
# Employee and AUTH_USER_MODEL are equal

@receiver(post_save, sender=Employee)
def create_employee_resume(sender, instance, created, **kwargs):
    """
    -------------------------------
    After save Employee in database
    -------------------------------
    """
    
    print("IN signal............")
    if created:
        print("... create resume ...")
        Resume.objects.create(employee=instance)
        # Role.objects.create(employee=instance)


@receiver(post_save, sender=Employee)
def save_employee_resume(sender, instance, **kwargs):
    instance.resume.save()
    logger.info(f"{instance}'s employee created with email {instance.email} and identifier {instance.identifier}")

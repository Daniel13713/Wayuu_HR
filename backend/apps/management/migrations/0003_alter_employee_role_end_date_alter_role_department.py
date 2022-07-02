# Generated by Django 4.0 on 2022-06-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_role',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='Date when employee end in role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='department',
            field=models.ManyToManyField(related_name='roles_by_department', through='management.Department_Role', to='management.Department'),
        ),
    ]
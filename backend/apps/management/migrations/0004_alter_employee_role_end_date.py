# Generated by Django 4.0 on 2022-06-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_employee_role_end_date_alter_role_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_role',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='Date when employee end in role', null=True),
        ),
    ]

# Generated by Django 4.0 on 2022-06-29 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['identifier'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
    ]
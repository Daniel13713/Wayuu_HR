# Generated by Django 4.0 on 2022-06-27 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sys_admin', '0001_initial'),
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='sys_admin.employee'),
        ),
        migrations.AddField(
            model_name='experience',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='sys_admin.employee'),
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='sys_admin.employee'),
        ),
    ]
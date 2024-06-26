# Generated by Django 5.0.4 on 2024-04-27 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_remove_empleados_area_remove_empleados_cargo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.cargo'),
        ),
        migrations.AlterField(
            model_name='areas',
            name='empleados',
            field=models.ManyToManyField(blank=True, limit_choices_to={'areas__isnull': True}, null=True, to='empresa.empleados'),
        ),
    ]

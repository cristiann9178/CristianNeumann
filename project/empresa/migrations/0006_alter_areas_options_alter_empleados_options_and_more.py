# Generated by Django 5.0.4 on 2024-04-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_empleados_cargo_alter_areas_empleados'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areas',
            options={'verbose_name': 'área', 'verbose_name_plural': 'áreas'},
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'empleado', 'verbose_name_plural': 'empleados'},
        ),
        migrations.AddField(
            model_name='empleados',
            name='documento',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='areas',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
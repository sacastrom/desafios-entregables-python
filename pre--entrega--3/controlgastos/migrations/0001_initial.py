# Generated by Django 4.2.7 on 2023-11-02 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaTransaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('mes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PresupuestoTransaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gasto_real', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('categoria_transaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlgastos.categoriatransaccion')),
            ],
        ),
    ]

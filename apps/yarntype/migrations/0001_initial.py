# Generated by Django 3.1 on 2020-12-04 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spinningmills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YarnType',
            fields=[
                ('yarntype_id', models.AutoField(primary_key=True, serialize=False)),
                ('yarntype_name', models.CharField(max_length=30, verbose_name='Nombre de Producto')),
                ('bag_volumen', models.IntegerField(default=0, verbose_name='Nro Bolsas')),
                ('kg_volumen', models.IntegerField(default=0, verbose_name='Kg')),
                ('yarntype_enabled', models.IntegerField(default=1, verbose_name='Habilitado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('spinningmills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spinningmills.spinningmills')),
            ],
        ),
    ]

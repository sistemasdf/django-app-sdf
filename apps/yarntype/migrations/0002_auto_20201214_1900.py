# Generated by Django 3.1 on 2020-12-15 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yarntype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarntype',
            name='kg_volumen',
            field=models.FloatField(default=0.0, verbose_name='Kg'),
        ),
    ]

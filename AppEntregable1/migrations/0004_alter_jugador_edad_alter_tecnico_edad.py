# Generated by Django 4.1.3 on 2022-12-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregable1', '0003_equipo_jugador_tecnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]

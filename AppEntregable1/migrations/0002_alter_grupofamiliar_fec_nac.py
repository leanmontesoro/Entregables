# Generated by Django 4.1.3 on 2022-11-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregable1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fec_nac',
            field=models.DateField(default='2022-00-00'),
        ),
    ]
